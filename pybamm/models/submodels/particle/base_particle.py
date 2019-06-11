#
# Base class for particles
#
import pybamm


class BaseParticle(pybamm.BaseSubModel):
    """Base class for molar conservation in particles.

    Parameters
    ----------
    param : parameter class
        The parameters to use for this submodel
    domain : str
        The domain of the model either 'Negative' or 'Positive'

    *Extends:* :class:`pybamm.BaseSubModel`
    """

    def __init__(self, param, domain):
        super().__init__(param)
        self._domain = domain

    def get_standard_derived_variables(self, variables):

        c_s = variables[self._domain + " particle concentration"]
        c_s_xav = variables[
            "X-average " + self._domain.lower() + " particle concentration"
        ]

        c_s_surf = pybamm.surf(c_s)
        c_s_surf_av = pybamm.average(c_s_surf)

        N_s = self._ficks_law(c_s)
        N_s_xav = self._ficks_law(c_s_xav)

        if self._domain == "Negative":
            ocp = self.param.U_n(c_s_surf)
            dudT = self.param.dUdT_n(c_s_surf)

        elif self._domain == "Positive":
            ocp = self.param.U_p(c_s_surf)
            dudT = self.param.dUdT_p(c_s_surf)

        else:
            pybamm.DomainError

        ocp_av = pybamm.average(ocp)
        dudT_av = pybamm.average(dudT)

        variables.update(
            {
                self._domain + " particle flux": N_s,
                "X-average " + self._domain.lower() + " particle flux": N_s_xav,
                self._domain + " particle surface concentration": c_s_surf,
                "Average "
                + self._domain.lower()
                + " particle surface concentration": c_s_surf_av,
                self._domain + " open circuit potential": ocp,
                "Average " + self._domain.lower() + " open circuit potential": ocp_av,
                self._domain + " entropic change": dudT,
                "Average " + self._domain.lower() + " entropic change": dudT_av,
            }
        )

        variables.update(self.get_dimensional_variables(variables))
        return variables

    def _flux_law(self, c):
        raise NotImplementedError

    def _unpack(self, variables):
        raise NotImplementedError

    def get_dimensional_variables(self, variables):

        c_s = variables[self._domain + " particle concentration"]
        c_s_xav = variables[
            "X-average " + self._domain.lower() + " particle concentration"
        ]
        c_s_surf = variables[self._domain + " particle surface concentration"]
        c_s_surf_av = variables[
            "Average " + self._domain.lower() + " particle surface concentration"
        ]

        if self._domain == "Negative":
            c_scale = self.param.c_n_max
        elif self._domain == "Positive":
            c_scale = self.param.c_p_max

        variables.update(
            {
                self._domain + " particle concentration [mol.m-3]": c_scale * c_s,
                "X-average "
                + self._domain.lower()
                + " particle concentration [mol.m-3]": c_scale * c_s_xav,
                self._domain
                + " particle surface concentration [mol.m-3]": c_scale * c_s_surf,
                "Average "
                + self._domain.lower()
                + " particle surface concentration [mol.m-3]": c_scale * c_s_surf_av,
            }
        )

        return variables

    def _initial_conditions(self, variables):

        c, _, _ = self._unpack(variables)

        if self._domain == "Negative":
            c_init = self.param.c_n_init

        elif self._domain == "Positive":
            c_init = self.param.c_p_init

        else:
            pybamm.DomainError

        initial_conditions = {c: c_init}

        return initial_conditions

