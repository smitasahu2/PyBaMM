import pybamm
from numpy import pi


class InverseButlerVolmer(pybamm.interface.BaseInterface):
    """
    A submodel that implements the inverted form of the Butler-Volmer relation to
    solve for the reaction overpotential.

    Parameters
    ----------
    param
        Model parameters
    domain : iter of str, optional
        The domain(s) in which to compute the interfacial current.
    reaction : str
        The name of the reaction being implemented
    options: dict
        A dictionary of options to be passed to the model. In this case "SEI film
        resistance" is the important option. See :class:`pybamm.BaseBatteryModel`

    **Extends:** :class:`pybamm.interface.BaseInterface`

    """

    def __init__(self, param, domain, reaction, options=None):
        super().__init__(param, domain, reaction, options=options)

    def get_coupled_variables(self, variables):
        domain, Domain = self.domain_Domain
        reaction_name = self.reaction_name

        ocp = variables[f"{Domain} electrode {reaction_name}open circuit potential"]

        j0 = self._get_exchange_current_density(variables)
        j_tot_av, a_j_tot_av = self._get_average_total_interfacial_current_density(
            variables
        )
        # Broadcast to match j0's domain
        if j0.domain in [[], ["current collector"]]:
            j_tot = j_tot_av
        else:
            j_tot = pybamm.PrimaryBroadcast(j_tot_av, [f"{domain} electrode"])
        variables.update(
            self._get_standard_total_interfacial_current_variables(j_tot, a_j_tot_av)
        )

        # Note: T and u must have the same domain as j0 and eta_r
        if self.options.electrode_types[domain] == "planar":
            T = variables["X-averaged cell temperature"]
            u = variables["Lithium metal interface utilisation"]
        elif j0.domain in ["current collector", ["current collector"]]:
            T = variables["X-averaged cell temperature"]
            u = variables[f"X-averaged {domain} electrode interface utilisation"]
        else:
            T = variables[f"{Domain} electrode temperature"]
            u = variables[f"{Domain} electrode interface utilisation"]

        # eta_r is the overpotential from inverting Butler-Volmer, regardless of any
        # additional resistance (e.g. SEI). What changes is how delta_phi is defined
        # in terms of eta_r
        ne = self._get_number_of_electrons_in_reaction()
        eta_r = self._get_overpotential(j_tot, j0, ne, T, u)

        # With SEI resistance (distributed and averaged have the same effect here)
        if self.domain == "negative":
            if self.options["SEI film resistance"] != "none":
                R_sei = self.phase_param.R_sei
                if self.options.electrode_types["negative"] == "planar":
                    L_sei = variables["Total SEI thickness"]
                else:
                    L_sei = variables["X-averaged total SEI thickness"]
                eta_sei = -j_tot * L_sei * R_sei
            # Without SEI resistance
            else:
                eta_sei = pybamm.Scalar(0)
            variables.update(
                self._get_standard_sei_film_overpotential_variables(eta_sei)
            )
        else:
            eta_sei = pybamm.Scalar(0)

        # add "mechanics overpotential"
        c = variables[f"{Domain} particle surface concentration [mol.m-3]"]
        eta_m = self._get_mechanics_overpotential(c)

        # define surface potential difference
        delta_phi = eta_m + eta_r + ocp - eta_sei  # = phi_s - phi_e

        variables.update(self._get_standard_exchange_current_variables(j0))
        variables.update(self._get_standard_overpotential_variables(eta_r))
        variables.update(
            self._get_standard_average_surface_potential_difference_variables(
                pybamm.x_average(delta_phi)
            )
        )

        return variables

    def _get_overpotential(self, j, j0, ne, T, u):
        # Linearised Butler-Volmer
        return (2 * (1 + self.param.Theta * T) / ne) * (j / (2 * j0 * u))

    def _get_mechanics_overpotential(self, c):
        _, Domain = self.domain_Domain
        param = self.param
        pot_scale = param.potential_scale  # potential scale [V]
        F = param.F  # Faraday constant [C.mol-1]
        Omega = self.domain_param.Omega  # partial molar volume [m3.mol-1]
        mu = pybamm.Parameter(f"{Domain} electrode Lame parameter [Pa]")
        R = self.phase_param.R_dimensional  # particle radius [m]
        Gamma_int = 4 * pi * R**2  # surface area [m2]
        nu = mu * Omega / F / pot_scale

        c_max = self.phase_param.c_max
        S_tot_dim = pybamm.FunctionParameter(
            f"{Domain} electrode volumetric stress [Pa]",
            {"Concentration [mol.m-3]": c, "Maximum concentration [mol.m-3]": c_max},
        )
        S_tot = S_tot_dim / mu / Gamma_int

        return nu * S_tot


class MSPM(pybamm.lithium_ion.SPM):
    """
    Single Particle Model of a lithium-ion battery from [1]_, with mechanics.

    Parameters
    ----------
    options : dict, optional
        A dictionary of options to be passed to the model. For a detailed list of
        options see :class:`~pybamm.BatteryModelOptions`.
    name : str, optional
        The name of the model.
    build :  bool, optional
        Whether to build the model on instantiation. Default is True. Setting this
        option to False allows users to change any number of the submodels before
        building the complete model (submodels cannot be changed after the model is
        built).

    References
    ----------
    .. [1] SG Marquis, V Sulzer, R Timms, CP Please and SJ Chapman. “An asymptotic
           derivation of a single particle model with electrolyte”. Journal of The
           Electrochemical Society, 166(15):A3693–A3706, 2019

    **Extends:** :class:`pybamm.lithium_ion.SPM`
    """

    def __init__(self, options=None, name="MSPM", build=True):
        # Check options
        options = options or {}
        kinetics = options.get("intercalation kinetics")
        if kinetics is not None:
            raise pybamm.OptionError("Cannot set 'intercalation kinetics' for MSPM.")
        options["x-average side reactions"] = "true"

        super().__init__(options=options, name=name, build=build)

    def set_intercalation_kinetics_submodel(self):

        for domain in ["negative", "positive"]:
            electrode_type = self.options.electrode_types[domain]
            if electrode_type == "planar":
                continue

            self.submodels[f"{domain} interface"] = InverseButlerVolmer(
                self.param, domain, "lithium-ion main", self.options
            )
            self.submodels[
                f"{domain} interface current"
            ] = pybamm.kinetics.CurrentForInverseButlerVolmer(
                self.param, domain, "lithium-ion main", self.options
            )
