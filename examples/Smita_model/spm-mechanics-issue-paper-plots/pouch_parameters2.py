import pybamm

def graphite_mcmb2528_diffusivity_Dualfoil1998(sto, T):
    """
    Graphite MCMB 2528 diffusivity as a function of stochiometry, in this case the
    diffusivity is taken to be a constant. The value is taken from Dualfoil [1].

    References
    ----------
    .. [1] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    sto: :class:`pybamm.Symbol`
        Electrode stochiometry
    T: :class:`pybamm.Symbol`
        Dimensional temperature

    Returns
    -------
    :class:`pybamm.Symbol`
        Solid diffusivity
    """

    D_ref = 3.9 * 10 ** (-14)
    E_D_s = 42770
    arrhenius = pybamm.exp(E_D_s / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return D_ref * arrhenius


def graphite_mcmb2528_ocp_Dualfoil1998(sto):
  
    """
    Graphite MCMB 2528 Open Circuit Potential (OCP) as a function of the
    stochiometry. The fit is taken from Dualfoil [1]. Dualfoil states that the data
    was measured by Chris Bogatu at Telcordia and PolyStor materials, 2000. However,
    we could not find any other records of this measurment.

    References
    ----------
    .. [1] http://www.cchem.berkeley.edu/jsngrp/fortran.html
    """
##    u_eq = (
##        0.194
##        + 1.5 * pybamm.exp(-120.0 * sto)
##        + 0.0351 * pybamm.tanh((sto - 0.286) / 0.083)
##        - 0.0045 * pybamm.tanh((sto - 0.849) / 0.119)
##        - 0.035 * pybamm.tanh((sto - 0.9233) / 0.05)
##        - 0.0147 * pybamm.tanh((sto - 0.5) / 0.034)
##        - 0.102 * pybamm.tanh((sto - 0.194) / 0.142)
##        - 0.022 * pybamm.tanh((sto - 0.9) / 0.0164)
##        - 0.011 * pybamm.tanh((sto - 0.124) / 0.0226)
##        + 0.0155 * pybamm.tanh((sto - 0.105) / 0.029)
##    )

    sto = 1-sto
    A0 = 0.124
    A1 = -0.8428
    B1 = -80.2493
    C1 = 1.3198
    A2 = -3.2474E-6
    B2 = 20.2645
    C2 = 3.8003
    A3 = 3.2482E-6
    B3 = 20.2646
    C3 = 3.7995
    u_eq = A0 + A1*pybamm.exp(B1*sto**C1) + A2*pybamm.exp(B2*sto**C2) + A3*pybamm.exp(B3*sto**C3)

    return u_eq


def graphite_electrolyte_exchange_current_density_Dualfoil1998(
    c_e, c_s_surf, c_s_max, T
):
    """
    Exchange-current density for Butler-Volmer reactions between graphite and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [2] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    c_s_max : :class:`pybamm.Symbol`
        Maximum particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """
    m_ref = 1* 10 ** (-5)#2 * 10 ** (-5)  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
    E_r = 37480
    arrhenius = pybamm.exp(E_r / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return (
        m_ref * arrhenius * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5
    )


def lico2_diffusivity_Dualfoil1998(sto, T):
    """
    LiCo2 diffusivity as a function of stochiometry, in this case the
    diffusivity is taken to be a constant. The value is taken from Dualfoil [1].

    References
    ----------
    .. [1] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    sto: :class:`pybamm.Symbol`
        Electrode stochiometry
    T: :class:`pybamm.Symbol`
        Dimensional temperature

    Returns
    -------
    :class:`pybamm.Symbol`
        Solid diffusivity
    """
    D_ref = 1 * 10 ** (-13)
    E_D_s = 18550
    arrhenius = pybamm.exp(E_D_s / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return D_ref * arrhenius


def lico2_ocp_Dualfoil1998(sto):
##    stretch = 1.062
##    sto = stretch * sto

    # u_eq = (
    #     2.16216
    #     + 0.07645 * pybamm.tanh(30.834 - 54.4806 * sto)
    #     + 2.1581 * pybamm.tanh(52.294 - 50.294 * sto)
    #     - 0.14169 * pybamm.tanh(11.0923 - 19.8543 * sto)
    #     + 0.2051 * pybamm.tanh(1.4684 - 5.4888 * sto)
    #     + 0.2531 * pybamm.tanh((-sto + 0.56478) / 0.1316)
    #     - 0.02167 * pybamm.tanh((sto - 0.525) / 0.006)
    # )  
        #u_eq = 3.4077 + 0.5 * pybamm.exp(-150 * sto) - 0.9 * pybamm.exp(-300 * (1-sto))
    sto = 1-sto
    A0 = 3.4323
    A1 = -0.8428
    B1 = -80.2493
    C1 = 1.3198
    A2 = -3.2474E-6
    B2 = 20.2645
    C2 = 3.8003
    A3 = 3.2482E-6
    B3 = 20.2646
    C3 = 3.7995
    
    u_eq = A0 + A1*pybamm.exp(B1*sto**C1) + A2*pybamm.exp(B2*sto**C2) + A3*pybamm.exp(B3*sto**C3)

    return u_eq





def lico2_electrolyte_exchange_current_density_Dualfoil1998(c_e, c_s_surf, c_s_max, T):
    """
    Exchange-current density for Butler-Volmer reactions between lico2 and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [2] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    c_e : :class:`pybamm.Symbol`
        Electrolyte concentration [mol.m-3]
    c_s_surf : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    c_s_max : :class:`pybamm.Symbol`
        Maximum particle concentration [mol.m-3]
    T : :class:`pybamm.Symbol`
        Temperature [K]

    Returns
    -------
    :class:`pybamm.Symbol`
        Exchange-current density [A.m-2]
    """
    m_ref = 6 * 10 ** (-7)  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
    E_r = 39570
    arrhenius = pybamm.exp(E_r / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return (
        m_ref * arrhenius * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5
    )


def electrolyte_diffusivity_Capiglia1999(c_e, T):
    """
    Diffusivity of LiPF6 in EC:DMC as a function of ion concentration. The original data
    is from [1]. The fit from Dualfoil [2].

    References
    ----------
    .. [1] C Capiglia et al. 7Li and 19F diffusion coefficients and thermal
    properties of non-aqueous electrolyte solutions for rechargeable lithium batteries.
    Journal of power sources 81 (1999): 859-862.
    .. [2] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    c_e: :class:`pybamm.Symbol`
        Dimensional electrolyte concentration
    T: :class:`pybamm.Symbol`
        Dimensional temperature


    Returns
    -------
    :class:`pybamm.Symbol`
        Solid diffusivity
    """

    D_c_e = 5.34e-10 * pybamm.exp(-0.65 * c_e / 1000)
    E_D_e = 37040
    arrhenius = pybamm.exp(E_D_e / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return D_c_e * arrhenius


def electrolyte_conductivity_Capiglia1999(c_e, T):
    """
    Conductivity of LiPF6 in EC:DMC as a function of ion concentration. The original
    data is from [1]. The fit is from Dualfoil [2].

    References
    ----------
    .. [1] C Capiglia et al. 7Li and 19F diffusion coefficients and thermal
    properties of non-aqueous electrolyte solutions for rechargeable lithium batteries.
    Journal of power sources 81 (1999): 859-862.
    .. [2] http://www.cchem.berkeley.edu/jsngrp/fortran.html

    Parameters
    ----------
    c_e: :class:`pybamm.Symbol`
        Dimensional electrolyte concentration
    T: :class:`pybamm.Symbol`
        Dimensional temperature
   sigma_e = (
        0.1297 * (c_e / 1000) ** 3 - 2.51 * (c_e / 1000) ** 1.5 + 3.329 * (c_e / 1000)
    )

    # Nyman et al. (2008) does not provide temperature dependence

    return sigma_e


    Returns
    -------
    :class:`pybamm.Symbol`
        Solid diffusivity
    """

    sigma_e = (
        0.0911
        + 1.9101 * (c_e / 1000)
        - 1.052 * (c_e / 1000) ** 2
        + 0.1554 * (c_e / 1000) ** 3
    )

    E_k_e = 34700
    arrhenius = pybamm.exp(E_k_e / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return sigma_e * arrhenius


def graphite_volumetric_stress(c_s, c_s_max):
    """
    Placeholder function for volumetric stress.

    Parameters
    ----------
    c_s : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    c_s_max : :class:`pybamm.Symbol`
        Maximum particle concentration [mol.m-3]

    Returns
    -------
    :class:`pybamm.Symbol`
        Volumetric stress [Pa]
    """
    return -16.3726*1e-5* (0.02 * c_s_max - c_s)


def lco_volumetric_stress(c_s, c_s_max):
    """
    Placeholder function for volumetric stress.

    Parameters
    ----------
    c_s : :class:`pybamm.Symbol`
        Particle concentration [mol.m-3]
    c_s_max : :class:`pybamm.Symbol`
        Maximum particle concentration [mol.m-3]

    Returns
    -------
    :class:`pybamm.Symbol`
        Volumetric stress [Pa]
    """
    return -2.72789*1e-3*  (0.95 * c_s_max - c_s)*0


# Call dict via a function to avoid errors when editing in place
def get_parameter_values():
    """
    Note: this parameter set does not claim to be representative of the true parameter
    values. Instead these are parameter values that were used to fit SEI models to
    observed experimental data in the referenced papers.
    """

    return {
        # cell
        "Negative current collector thickness [m]": 2.5e-05,
        "Negative electrode thickness [m]": 0.0001,
        "Separator thickness [m]": 2.5e-05,
        "Positive electrode thickness [m]": 0.0001,
        "Positive current collector thickness [m]": 2.5e-05,
        "Electrode height [m]": 0.137,
        "Electrode width [m]": 0.207,
        "Negative tab width [m]": 0.04,
        "Negative tab centre y-coordinate [m]": 0.06,
        "Negative tab centre z-coordinate [m]": 0.137,
        "Positive tab width [m]": 0.04,
        "Positive tab centre y-coordinate [m]": 0.147,
        "Positive tab centre z-coordinate [m]": 0.137,
        "Cell cooling surface area [m2]": 0.0569,
        "Cell volume [m3]": 7.8e-06,
        "Negative current collector conductivity [S.m-1]": 596000.0,
        "Positive current collector conductivity [S.m-1]": 35500000.0,
        "Nominal cell capacity [A.h]": 0.680616,
        "Typical current [A]": 0.680616,
        "Current function [A]": 0.680616,
        # negative electrode
        "Negative electrode conductivity [S.m-1]": 100.0,
        "Maximum concentration in negative electrode [mol.m-3]":  24983.261993843,
        "Negative electrode diffusivity [m2.s-1]"
        "": graphite_mcmb2528_diffusivity_Dualfoil1998,
        "Negative electrode OCP [V]": graphite_mcmb2528_ocp_Dualfoil1998,
        "Negative electrode porosity": 0.3,
        "Negative electrode active material volume fraction": 0.6,
        "Negative particle radius [m]": 1e-05,
        "Negative electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Negative electrode Bruggeman coefficient (electrode)": 1.5,
        "Negative electrode cation signed stoichiometry": -1.0,
        "Negative electrode electrons in reaction": 1.0,
        "Negative electrode charge transfer coefficient": 0.5,
        "Negative electrode double-layer capacity [F.m-2]": 0.2,
        "Negative electrode exchange-current density [A.m-2]"
        "": graphite_electrolyte_exchange_current_density_Dualfoil1998,
        "Negative electrode OCP entropic change [V.K-1]": 0.0,
        "Negative electrode Lame parameter [Pa]": 1e8,
        "Negative electrode partial molar volume [m3.mol-1]": 3.1e-06,
        "Negative electrode volumetric stress [Pa]": graphite_volumetric_stress,
        # positive electrode
        "Positive electrode conductivity [S.m-1]": 0.33795074,
        "Maximum concentration in positive electrode [mol.m-3]": 51217.9257309275,
        "Positive electrode diffusivity [m2.s-1]": lico2_diffusivity_Dualfoil1998,
        "Positive electrode OCP [V]": lico2_ocp_Dualfoil1998,
        "Positive electrode porosity": 0.12728395,
        "Positive electrode active material volume fraction": 0.28485556,
        "Positive particle radius [m]": 1e-08,
        "Positive electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Positive electrode Bruggeman coefficient (electrode)": 1.5,
        "Positive electrode cation signed stoichiometry": -1.0,
        "Positive electrode electrons in reaction": 1.0,
        "Positive electrode charge transfer coefficient": 0.5,
        "Positive electrode double-layer capacity [F.m-2]": 0.2,
        "Positive electrode exchange-current density [A.m-2]"
        "": lico2_electrolyte_exchange_current_density_Dualfoil1998,
        "Positive electrode OCP entropic change [V.K-1]": 0.0,
        "Positive electrode Lame parameter [Pa]": 1e8,
        "Positive electrode partial molar volume [m3.mol-1]":2.9e-6, #-7.28e-07,
        "Positive electrode volumetric stress [Pa]": lco_volumetric_stress,
        # separator
        "Separator porosity": 1.0,
        "Separator Bruggeman coefficient (electrolyte)": 1.5,
        # electrolyte
        "Typical electrolyte concentration [mol.m-3]": 1000.0,
        "Initial concentration in electrolyte [mol.m-3]": 1000.0,
        "Cation transference number": 0.4,
        "1 + dlnf/dlnc": 1.0,
        "Electrolyte diffusivity [m2.s-1]": electrolyte_diffusivity_Capiglia1999,
        "Electrolyte conductivity [S.m-1]": electrolyte_conductivity_Capiglia1999,
        # experiment
        "Reference temperature [K]": 298.15,
        "Ambient temperature [K]": 298.15,
        "Number of electrodes connected in parallel to make a cell": 1.0,
        "Number of cells connected in series to make a battery": 1.0,
        "Lower voltage cut-off [V]":2.7,#,€3.105,
        "Upper voltage cut-off [V]":3.4,#  4.1,
#        "Initial concentration in negative electrode [mol.m-3]":4996.6523987686,# 21235.77269476655, #discharge 85% full  #charge 4996.6523987686, #20% full #1986, #19986.609595075,
#        "Initial concentration in positive electrode [mol.m-3]":30730.755438556498,#  10243.5851461855, #discharge 20% full  #charge 30730.755438556498,# 60%40974.340584742, # 80% full
#         "Initial concentration in negative electrode [mol.m-3]": 21235.6523987686,
        # "Initial concentration in positive electrode [mol.m-3]": 30730.755438556498,
        "Initial concentration in negative electrode [mol.m-3]": 2000,
        "Initial concentration in positive electrode [mol.m-3]": 50000,

        "Initial temperature [K]": 298.15,
    }
