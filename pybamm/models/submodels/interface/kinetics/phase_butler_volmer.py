#
# Bulter volmer class for the MSMR formulation
#

import pybamm
from .base_kinetics import BaseKinetics


class PhaseButlerVolmer(BaseKinetics):
    """
    Submodel which implements the forward Butler-Volmer equation in the MSMR
    formulation in which the interfacial current density is summed over all
    reactions.

    Parameters
    ----------
    param : parameter class
        model parameters
    domain : str
        The domain to implement the model, either: 'Negative' or 'Positive'.
    reaction : str
        The name of the reaction being implemented
    options: dict
        A dictionary of options to be passed to the model.
        See :class:`pybamm.BaseBatteryModel`
    phase : str, optional
        Phase of the particle (default is "primary")
    """

    def __init__(self, param, domain, reaction, options, phase="primary"):
        super().__init__(param, domain, reaction, options, phase)

    def _get_exchange_current_density_phase(self, variables):
        domain, Domain = self.domain_Domain
        # T = variables[f"{Domain} electrode temperature [K]"]
        # c_e = variables[f"{Domain} electrolyte concentration [mol.m-3]"]
        c_s_rav = variables[f"R-averaged {domain} particle concentration [mol.m-3]"]
        c_s_max = 22806.0

        k = 1.6e-7
        # om = 3.5
        # mu_Li = (
        #     pybamm.constants.R
        #     * T
        #     * (
        #         pybamm.log((c_s_rav / c_s_max) / (1 - c_s_rav / c_s_max))
        #         + om * (1 - 2 * c_s_rav / c_s_max)
        #     )
        # )
        # j0 = k * pybamm.exp(mu_Li / pybamm.constants.R / T / 2) * c_e**0.5
        j0 = k * (1 - c_s_rav / c_s_max) ** 0.5 * (c_s_rav / c_s_max) ** 0.5
        return j0

    def _get_phi_eq(self, variables):
        domain, Domain = self.domain_Domain
        T = variables[f"{Domain} electrode temperature [K]"]
        c_s_rav = variables[f"R-averaged {domain} particle concentration [mol.m-3]"]
        c_s_max = 22806.0
        om = 3.5

        # equation 13
        mu_Li = (
            pybamm.constants.R
            * T
            * (
                pybamm.log((c_s_rav / c_s_max) / (1 - c_s_rav / c_s_max))
                + om * (1 - 2 * c_s_rav / c_s_max)
            )
        )
        mu_Li_plus = -328873.86163228
        mu_e_0 = 0

        phi_eq = 1 / pybamm.constants.F * (mu_Li - mu_Li_plus - mu_e_0)
        return phi_eq

    def _get_kinetics_phase(self, j0, ne, eta_r, T, u):
        Feta_RT = self.param.F * eta_r / (self.param.R * T)
        return 2 * u * j0 * pybamm.sinh(ne * 0.5 * Feta_RT)
