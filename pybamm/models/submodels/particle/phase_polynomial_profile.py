#
# Class for many particles with polynomial concentration profile
#
import pybamm

from .base_particle import BaseParticle


class PhasePolynomialProfile(BaseParticle):
    """
    Class for molar conservation in particles employing Fick's
    law, assuming a polynomial concentration profile in r, and allowing variation
    in the electrode domain. Model equations from :footcite:t:`Subramanian2005`.

    Parameters
    ----------
    param : parameter class
        The parameters to use for this submodel
    domain : str
        The domain of the model either 'Negative' or 'Positive'
    options: dict
        A dictionary of options to be passed to the model.
        See :class:`pybamm.BaseBatteryModel`
    phase : str, optional
        Phase of the particle (default is "primary")

    """

    def __init__(self, param, domain, options, phase="primary"):
        super().__init__(param, domain, options, phase)
        self.name = getattr(self.options, self.domain)["particle"]
        if self.name == "Fickian diffusion":
            raise ValueError("Particle type must be 'phase averaged' ")

        # pybamm.citations.register("Subramanian2005")

    def get_fundamental_variables(self):
        domain, Domain = self.domain_Domain

        variables = {}
        # For all orders we solve an equation for the average concentration
        if self.size_distribution is False:
            c_s_rav = pybamm.Variable(
                f"R-averaged {domain} particle concentration [mol.m-3]",
                domain=f"{domain} electrode",
                auxiliary_domains={"secondary": "current collector"},
                bounds=(0, self.phase_param.c_max),
                scale=self.phase_param.c_max,
            )
            R = self.phase_param.R
        else:
            c_s_rav_distribution = pybamm.Variable(
                f"R-averaged {domain} particle concentration distribution [mol.m-3]",
                domain=f"{domain} particle size",
                auxiliary_domains={
                    "secondary": f"{domain} electrode",
                    "tertiary": "current collector",
                },
                bounds=(0, self.phase_param.c_max),
                scale=self.phase_param.c_max,
            )
            R = pybamm.SpatialVariable(
                f"R_{domain[0]}",
                domain=[f"{domain} particle size"],
                auxiliary_domains={
                    "secondary": f"{domain} electrode",
                    "tertiary": "current collector",
                },
                coord_sys="cartesian",
            )

            variables = self._get_distribution_variables(R)

            # Standard concentration distribution variables (size-dependent)
            variables.update(
                self._get_standard_concentration_distribution_variables(
                    c_s_rav_distribution
                )
            )

            # Standard size-averaged variables. Average concentrations using
            # the volume-weighted distribution since they are volume-based
            # quantities. Necessary for output variables "Total lithium in
            # negative electrode [mol]", etc, to be calculated correctly
            f_v_dist = variables[
                f"{Domain} volume-weighted particle-size distribution [m-1]"
            ]
            c_s_rav = pybamm.Integral(f_v_dist * c_s_rav_distribution, R)
            c_s_surf = c_s_rav
            c_s = pybamm.PrimaryBroadcast(c_s_rav, [f"{domain} particle"])

            variables.update(
                self._get_standard_concentration_variables(
                    c_s, c_s_rav=c_s_rav, c_s_surf=c_s_surf
                )
            )

            return variables

        if self.name == "phase averaged":
            # The concentration is uniform so the surface value is equal to
            # the average
            c_s_surf = c_s_rav
            A = c_s_rav

        A = pybamm.PrimaryBroadcast(A, [f"{domain} particle"])
        c_s = A
        variables.update(
            self._get_standard_concentration_variables(
                c_s, c_s_rav=c_s_rav, c_s_surf=c_s_surf
            )
        )

        return variables

    def get_coupled_variables(self, variables):
        domain, Domain = self.domain_Domain

        if self.size_distribution is False:
            pass
        else:
            # only uniform concentration implemented, no need to calculate D_eff
            pass

        # Set flux depending on polynomial order

        if self.name == "phase averaged":
            # The flux is zero since there is no concentration gradient
            N_s = pybamm.FullBroadcastToEdges(
                0,
                [f"{domain} particle"],
                auxiliary_domains={
                    "secondary": f"{domain} electrode",
                    "tertiary": "current collector",
                },
            )

        variables.update(self._get_standard_flux_variables(N_s))

        return variables

    def set_rhs(self, variables):
        domain, Domain = self.domain_Domain

        if self.size_distribution is False:
            c_s_rav = variables[f"R-averaged {domain} particle concentration [mol.m-3]"]
            j = variables[f"{Domain} electrode interfacial current density [A.m-2]"]
            R = variables[f"{Domain} particle radius [m]"]
        else:
            c_s_rav = variables[
                f"R-averaged {domain} particle concentration distribution [mol.m-3]"
            ]
            j = variables[
                f"{Domain} electrode interfacial current density distribution [A.m-2]"
            ]
            R = variables[f"{Domain} particle sizes [m]"]

        self.rhs = {c_s_rav: -3 * j / self.param.F / R}

    def set_algebraic(self, variables):
        if self.name == "phase averaged":
            # We solve an algebraic equation for the surface concentration
            return

    def set_initial_conditions(self, variables):
        domain, Domain = self.domain_Domain

        c_init = pybamm.r_average(self.phase_param.c_init)

        if self.size_distribution is False:
            c_s_rav = variables[f"R-averaged {domain} particle concentration [mol.m-3]"]
        else:
            c_s_rav = variables[
                f"R-averaged {domain} particle concentration distribution [mol.m-3]"
            ]
            c_init = pybamm.PrimaryBroadcast(c_init, [f"{domain} particle size"])

        self.initial_conditions = {c_s_rav: c_init}
