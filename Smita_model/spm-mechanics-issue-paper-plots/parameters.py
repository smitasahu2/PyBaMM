import pybamm


def graphite_LGM50_ocp_Chen2020(sto):
    """
    LG M50 Graphite open-circuit potential as a function of stochiometry, fit taken
    from [1].

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

    Parameters
    ----------
    sto: :class:`pybamm.Symbol`
        Electrode stochiometry

    Returns
    -------
    :class:`pybamm.Symbol`
        Open circuit potential
    """

    u_eq = (
        1.9793 * pybamm.exp(-39.3631 * sto)
        + 0.2482
        - 0.0909 * pybamm.tanh(29.8538 * (sto - 0.1234))
        - 0.04478 * pybamm.tanh(14.9159 * (sto - 0.2769))
        - 0.0205 * pybamm.tanh(30.4444 * (sto - 0.6103))
    )

    return u_eq


def graphite_LGM50_electrolyte_exchange_current_density_Chen2020(
    c_e, c_s_surf, c_s_max, T
):
    """
    Exchange-current density for Butler-Volmer reactions between graphite and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

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
    m_ref = 6.48e-7  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
    E_r = 35000
    arrhenius = pybamm.exp(E_r / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return (
        m_ref * arrhenius * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5
    )


def nmc_LGM50_ocp_Chen2020(sto):
    """
    LG M50 NMC open circuit potential as a function of stochiometry, fit taken
    from [1].

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

    Parameters
    ----------
    sto: :class:`pybamm.Symbol`
        Electrode stochiometry

    Returns
    -------
    :class:`pybamm.Symbol`
        Open circuit potential
    """

    u_eq = (
        -0.8090 * sto
        + 4.4875
        - 0.0428 * pybamm.tanh(18.5138 * (sto - 0.5542))
        - 17.7326 * pybamm.tanh(15.7890 * (sto - 0.3117))
        + 17.5842 * pybamm.tanh(15.9308 * (sto - 0.3120))
    )

    return u_eq


def nmc_LGM50_electrolyte_exchange_current_density_Chen2020(c_e, c_s_surf, c_s_max, T):
    """
    Exchange-current density for Butler-Volmer reactions between NMC and LiPF6 in
    EC:DMC.

    References
    ----------
    .. [1] Chang-Hui Chen, Ferran Brosa Planella, Kieran O’Regan, Dominika Gastol, W.
    Dhammika Widanage, and Emma Kendrick. "Development of Experimental Techniques for
    Parameterization of Multi-scale Lithium-ion Battery Models." Journal of the
    Electrochemical Society 167 (2020): 080534.

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
    m_ref = 3.42e-6  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
    E_r = 17800
    arrhenius = pybamm.exp(E_r / pybamm.constants.R * (1 / 298.15 - 1 / T))

    return (
        m_ref * arrhenius * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5
    )


def electrolyte_diffusivity_Nyman2008(c_e, T):
    """
    Diffusivity of LiPF6 in EC:EMC (3:7) as a function of ion concentration. The data
    comes from [1]

    References
    ----------
    .. [1] A. Nyman, M. Behm, and G. Lindbergh, "Electrochemical characterisation and
    modelling of the mass transport phenomena in LiPF6-EC-EMC electrolyte,"
    Electrochim. Acta, vol. 53, no. 22, pp. 6356–6365, 2008.

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

    D_c_e = 8.794e-11 * (c_e / 1000) ** 2 - 3.972e-10 * (c_e / 1000) + 4.862e-10

    # Nyman et al. (2008) does not provide temperature dependence

    return D_c_e


def electrolyte_conductivity_Nyman2008(c_e, T):
    """
    Conductivity of LiPF6 in EC:EMC (3:7) as a function of ion concentration. The data
    comes from [1].

    References
    ----------
    .. [1] A. Nyman, M. Behm, and G. Lindbergh, "Electrochemical characterisation and
    modelling of the mass transport phenomena in LiPF6-EC-EMC electrolyte,"
    Electrochim. Acta, vol. 53, no. 22, pp. 6356–6365, 2008.

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

    sigma_e = (
        0.1297 * (c_e / 1000) ** 3 - 2.51 * (c_e / 1000) ** 1.5 + 3.329 * (c_e / 1000)
    )

    # Nyman et al. (2008) does not provide temperature dependence

    return sigma_e


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
    return -16.3726*1e-5 * (0.02 * c_s_max - c_s)


def nmc_volumetric_stress(c_s, c_s_max):
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
    return -4.72789*1e-5 * (0.95 * c_s_max - c_s)


# Call dict via a function to avoid errors when editing in place
def get_parameter_values():
    """
    Parameters for an LG M50 cell, from the paper

        Chang-Hui Chen, Ferran Brosa Planella, Kieran O'Regan, Dominika Gastol, W.
        Dhammika Widanage, and Emma Kendrick. Development of Experimental Techniques for
        Parameterization of Multi-scale Lithium-ion Battery Models. Journal of The
        Electrochemical Society, 167(8):080534, 2020. doi:10.1149/1945-7111/ab9050.

    and references therein.

    SEI parameters are example parameters for SEI growth from the papers:

        Ramadass, P., Haran, B., Gomadam, P. M., White, R., & Popov, B. N. (2004).
        Development of first principles capacity fade model for Li-ion cells. Journal of
        the Electrochemical Society, 151(2), A196-A203.

        Ploehn, H. J., Ramadass, P., & White, R. E. (2004). Solvent diffusion model for
        aging of lithium-ion battery cells. Journal of The Electrochemical Society,
        151(3), A456-A462.

        Single, F., Latz, A., & Horstmann, B. (2018). Identifying the mechanism of
        continued growth of the solid-electrolyte interphase. ChemSusChem, 11(12),
        1950-1955.

        Safari, M., Morcrette, M., Teyssot, A., & Delacour, C. (2009). Multimodal
        Physics- Based Aging Model for Life Prediction of Li-Ion Batteries. Journal of
        The Electrochemical Society, 156(3),

        Yang, X., Leng, Y., Zhang, G., Ge, S., Wang, C. (2017). Modeling of lithium
        plating induced aging of lithium-ion batteries: Transition from linear to
        nonlinear aging. Journal of Power Sources, 360, 28-40.

    Note: this parameter set does not claim to be representative of the true parameter
    values. Instead these are parameter values that were used to fit SEI models to
    observed experimental data in the referenced papers.
    """

    return {
        # cell
        "Negative electrode thickness [m]": 8.52e-05,
        "Separator thickness [m]": 1.2e-05,
        "Positive electrode thickness [m]": 7.56e-05,
        "Electrode height [m]": 0.065,
        "Electrode width [m]": 1.58,
        "Nominal cell capacity [A.h]": 5.0,
        "Typical current [A]": 5.0,
        "Current function [A]": 5.0,
        # negative electrode
        "Negative electrode conductivity [S.m-1]": 215.0,
        "Maximum concentration in negative electrode [mol.m-3]": 33133.0,
        "Negative electrode diffusivity [m2.s-1]": 3.3e-14,
        "Negative electrode OCP [V]": graphite_LGM50_ocp_Chen2020,
        "Negative electrode porosity": 0.25,
        "Negative electrode active material volume fraction": 0.75,
        "Negative particle radius [m]": 5.86e-06,
        "Negative electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Negative electrode Bruggeman coefficient (electrode)": 1.5,
        "Negative electrode cation signed stoichiometry": -1.0,
        "Negative electrode electrons in reaction": 1.0,
        "Negative electrode charge transfer coefficient": 0.5,
        "Negative electrode exchange-current density [A.m-2]"
        "": graphite_LGM50_electrolyte_exchange_current_density_Chen2020,
        "Negative electrode OCP entropic change [V.K-1]": 0.0,
        "Negative electrode Lame parameter [Pa]": 1e8,
        "Negative electrode partial molar volume [m3.mol-1]": 3.1e-06,
        "Negative electrode volumetric stress [Pa]": graphite_volumetric_stress,
        # positive electrode
        "Positive electrode conductivity [S.m-1]": 0.18,
        "Maximum concentration in positive electrode [mol.m-3]": 63104.0,
        "Positive electrode diffusivity [m2.s-1]": 4e-15,
        "Positive electrode OCP [V]": nmc_LGM50_ocp_Chen2020,
        "Positive electrode porosity": 0.335,
        "Positive electrode active material volume fraction": 0.665,
        "Positive particle radius [m]": 5.22e-06,
        "Positive electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Positive electrode Bruggeman coefficient (electrode)": 1.5,
        "Positive electrode cation signed stoichiometry": -1.0,
        "Positive electrode electrons in reaction": 1.0,
        "Positive electrode charge transfer coefficient": 0.5,
        "Positive electrode double-layer capacity [F.m-2]": 0.2,
        "Positive electrode exchange-current density [A.m-2]"
        "": nmc_LGM50_electrolyte_exchange_current_density_Chen2020,
        "Positive electrode OCP entropic change [V.K-1]": 0.0,
        "Positive electrode Lame parameter [Pa]": 1e8,
        "Positive electrode partial molar volume [m3.mol-1]": -7.28e-07,
        "Positive electrode volumetric stress [Pa]": nmc_volumetric_stress,
        # separator
        "Separator porosity": 0.47,
        "Separator Bruggeman coefficient (electrolyte)": 1.5,
        # electrolyte
        "Typical electrolyte concentration [mol.m-3]": 1000.0,
        "Initial concentration in electrolyte [mol.m-3]": 1.0,
        "Cation transference number": 0.2594,
        "1 + dlnf/dlnc": 1.0,
        "Electrolyte diffusivity [m2.s-1]": electrolyte_diffusivity_Nyman2008,
        "Electrolyte conductivity [S.m-1]": electrolyte_conductivity_Nyman2008,
        # experiment
        "Reference temperature [K]": 298.15,
        "Ambient temperature [K]": 298.15,
        "Number of electrodes connected in parallel to make a cell": 1.0,
        "Number of cells connected in series to make a battery": 1.0,
        "Lower voltage cut-off [V]": 2.5,
        "Upper voltage cut-off [V]": 4.2,
        "Initial concentration in negative electrode [mol.m-3]": 29866.0,
        "Initial concentration in positive electrode [mol.m-3]": 17038.0,
        "Initial temperature [K]": 298.15,
    }
