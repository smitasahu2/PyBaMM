import pybamm
"""
   Here I am defining all the parameters from [1]
    [1] Paul Albertus, Jake Christensen, and John Newman. Experiments on
    and Modeling of Positive Electrodes with Multiple Active Materials for Lithium-Ion Batteries.
    Journal of The Electrochemical Society, 156(7):A606, 2009. doi: 10.1149/1.3129656.

    Primary active material is NCA
    Secondary active material is LMO
"""
def lmo_ocp_lithiation_Albertus2009(sto):
  """
  The fit is taken from the Enertech cell [1], which is only accurate
  for 0 < sto < 1.

  References
  ----------
  [1] Paul Albertus, Jake Christensen, and John Newman. Experiments on
     and Modeling of Positive Electrodes with Multiple Active Materials for Lithium-Ion Batteries.
     Journal of The Electrochemical Society, 156(7):A606, 2009. doi: 10.1149/1.3129656.

  Parameters
  ----------
  sto: double
  Stochiometry of material (li-fraction)

  Returns
  -------
  :class:`pybamm.Symbol`
   OCP [V] of LMO
  """

  p1 = -27.98
  p2 = 7.072
  p3 = 3.495
  p4 = 31.9
  p5 = -172.2
  p6 = -1.007
  p7 = -4.5
  p8 = 0.1
  p9=-1

  U_lithiation = (
     p1*pybamm.tanh(p2*(sto+p3))
    +p4*pybamm.tanh(p5*(sto+p6))
    +p7*pybamm.tanh(p8*(sto+p9))
    )
  
  return U_lithiation


def lmo_ocp_delithiation_Albertus2009(sto):
    """
    The fit is taken from the Enertech cell [1], which is only accurate
    for 0 < sto < 1.

    References
    ----------
    [1] Paul Albertus, Jake Christensen, and John Newman. Experiments on
     and Modeling of Positive Electrodes with Multiple Active Materials for Lithium-Ion Batteries.
     Journal of The Electrochemical Society, 156(7):A606, 2009. doi: 10.1149/1.3129656.

    Parameters
    ----------
    sto: double
    Stochiometry of material (li-fraction)

    Returns
    -------
    :class:`pybamm.Symbol`
    OCP [V] of LMO
    """

    p1 = -27.98
    p2 = 7.072
    p3 = 3.495
    p4 = 31.9
    p5 = -172.2
    p6 = -1.007
    p7 = -4.5
    p8 = 0.1
    p9=-1

    U_delithiation = (
     p1*pybamm.tanh(p2*(sto+p3))
    +p4*pybamm.tanh(p5*(sto+p6))
    +p7*pybamm.tanh(p8*(sto+p9))
    )
    
    return U_delithiation


def lmo_electrolyte_exchange_current_density_Albertus2009(c_e, c_s_surf, c_s_max, T):
    """
    Exchange-current density for Butler-Volmer reactions between silicon and LMO in
    EC:DMC.

    References
    ----------
    .. Fitted

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
    m_ref = 5.0e-10 # /  pybamm.constants.F

    return (
        m_ref * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5
    )

def nca_ocp_Albertus2009(sto):
    """
    The fit is taken from the Enertech cell [1], which is only accurate
    for 0 < sto < 1.

    References
    ----------
    [1] Paul Albertus, Jake Christensen, and John Newman. Experiments on
     and Modeling of Positive Electrodes with Multiple Active Materials for Lithium-Ion Batteries.
     Journal of The Electrochemical Society, 156(7):A606, 2009. doi: 10.1149/1.3129656.

    Parameters
    ----------
    sto: double
    Stochiometry of material (li-fraction)

    Returns
    -------
    :class:`pybamm.Symbol`
    OCP [V] of NCA
    """
    a1 =       3.987;        b1 =      0.3267
    c1 =      0.1024;        a2 =       1.691
    b2 =      0.4924;        c2 =     0.07473
    a3 =       3.252;        b3 =      0.5948
    c3 =       0.119;        a4 =       2.934
    b4 =      0.7576;        c4 =      0.1109
    a5 =       1.502;        b5 =      0.8466
    c5 =     0.06781;        a6 =       1.314
    b6 =      0.9037;        c6 =     0.05436
    a7 =       3.105;        b7 =      0.9799
    c7 =     0.07147;        a8 =       1.341
    b8 =      0.4247;        c8 =     0.06532
    
    u_eq = (
       a1*pybamm.exp(-((sto-b1)/c1)**2) + a2*pybamm.exp(-((sto-b2)/c2)**2)
      +a3*pybamm.exp(-((sto-b3)/c3)**2) + a4*pybamm.exp(-((sto-b4)/c4)**2)
      +a5*pybamm.exp(-((sto-b5)/c5)**2) + a6*pybamm.exp(-((sto-b6)/c6)**2) 
      +a7*pybamm.exp(-((sto-b7)/c7)**2) + a8*pybamm.exp(-((sto-b8)/c8)**2)
    )
    
    return u_eq


def nca_electrolyte_exchange_current_density_Albertus2009( c_e, c_s_surf, c_s_max, T): 
    """
    Exchange-current density for Butler-Volmer reactions between silicon and NCA in
    EC:DMC.

    References
    ----------
    .. Fitted

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
    m_ref = 1.0e-10 # / pybamm.constants.F  # (A/m2)(m3/mol)**1.5 - includes ref concentrations

    return (
        m_ref  * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5
    )




def nca_diffusivity_Albertus2009(sto,T):
    """
    NCO diffusivity as a function of stochiometry

    References
    ----------
    .. Fitted
    Parameters
    ----------
    sto : :class:`pybamm.Symbol`
       Stochiometry of material (li-fraction)

    """    
    sto = sto / 49459  # I think his cmax for nca is 49459

    Ds = 3.0e-15 * ( ( 1 + pybamm.tanh( -20 * ( sto - 0.73))) + 0.02)

    return Ds


def graphite_ocp_Enertech_Albertus2009(sto):

    """
      WE DON'T USE ITn
    References
    ----------
     .. [1] Ecker, Madeleine, et al. "Parameterization of a physico-chemical model of
    a lithium-ion battery i. determination of parameters." Journal of the
    Electrochemical Society 162.9 (2015): A1836-A1848.
    .. [2] Ecker, Madeleine, et al. "Parameterization of a physico-chemical model of
    a lithium-ion battery ii. model validation." Journal of The Electrochemical
    Society 162.9 (2015): A1849-A1857.
    .. [3] Richardson, Giles, et. al. "Generalised single particle models for
    high-rate operation of graded lithium-ion electrodes: Systematic derivation
    and validation." Electrochemica Acta 339 (2020): 135862

    Parameters
    ----------
    sto: :class:`pybamm.Symbol`
        Electrode stochiometry

    Returns
    -------
    :class:`pybamm.Symbol`
        Open circuit potential
    """

    # Graphite negative electrode from Ecker, Kabitz, Laresgoiti et al.
    # Analytical fit (WebPlotDigitizer + gnuplot)
    a = 0.716502
    b = 369.028
    c = 0.12193
    d = 35.6478
    e = 0.0530947
    g = 0.0169644
    h = 27.1365
    i = 0.312832#         "Typical electrolyte concentration [mol.m-3]": 1000.0,

    j = 0.0199313
    k = 28.5697
    m = 0.614221
    n = 0.931153
    o = 36.328
    p = 1.10743
    q = 0.140031
    r = 0.0189193
    s = 21.1967
    t = 0.196176

    u_eq = (
        a * pybamm.exp(-b * sto)
        + c * pybamm.exp(-d * (sto - e))
        - r * pybamm.tanh(s * (sto - t))
        - g * pybamm.tanh(h * (sto - i))
        - j * pybamm.tanh(k * (sto - m))
        - n * pybamm.exp(o * (sto - p))
        + q
    )
    return u_eq

def electrolyte_diffusivity_Albertus2009(c_e,T):
    """
    Diffusivity of LiPF6 in EC:DMC as a function of ion concentration [1, 2, 3].

    References
    ----------
    .. [1] Paul Albertus, Jake Christensen, and John Newman. Experiments on
     and Modeling of Positive Electrodes with Multiple Active Materials for Lithium-Ion Batteries.
     Journal of The Electrochemical Society, 156(7):A606, 2009. doi: 10.1149/1.3129656.

    Parameters
    ----------
    c_e: :class:`pybamm.Symbol`
        Dimensional electrolyte concentration
    T: :class:`pybamm.Symbol`
        Dimensional temperature

    Returns
    -------
    """

    D_c_e = 6.5e-10 * pybamm.exp(-0.7 * c_e / 1000)
#         "Typical electrolyte concentration [mol.m-3]": 1000.0,

def electrolyte_conductivity_Albertus2009(c_e,T):

    """
    Conductivity of LiPF6 in EC:DMC as a function of ion concentration [1, 2, 3].

    References
    ----------
    .. [1] Paul Albertus, Jake Christensen, and John Newman. Experiments on
     and Modeling of Positive Electrodes with Multiple Active Materials for Lithium-Ion Batteries.
     Journal of The Electrochemical Society, 156(7):A606, 2009. doi: 10.1149/1.3129656.

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
        0.84 * (0.1 + (1.134 * c_e / 1000) /(1.0 + 0.2 * (c_e / 1000) + 0.08 * (c_e / 1000) ** 4))
    )
  
    return sigma_e


# def nmc_LGM50_ocp_Chen2020(sto):
#     return 4*sto

#     # ## Ueq for NMC

#     # u_eq = (
#     #     -0.8090 * sto
#     #    + 4.4875
#     #    - 0.0428 * pybamm.tanh(18.5138 * (sto - 0.5542))
#     #    - 17.7326 * pybamm.tanh(15.7890 * (sto - 0.3117))
#     #     + 17.5842 * pybamm.tanh(15.9308 * (sto - 0.3120))
#     # ) 
#     # ## Ueq for NMC (custumized to make Ueq=0)
    
#     # #u_eq = (
#     #     #-0.8090 * sto*0.1
#     #     #+ 4.4875*0.9
#     #    #- 0.0428 * pybamm.tanh(18.5138 * (sto - 0.5542))*0
#     #   # - 17.7326 * pybamm.tanh(15.7890 * (sto - 0.3117))*0
#     #  #  + 17.5842 * pybamm.tanh(15.9308 * (sto - 0.3120))*0
#     # #)
# def nmc_LGM50_electrolyte_exchange_current_density_Chen2020(c_e, c_s_surf, c_s_max, T):
#   return 1000.0000
   

#     # #m_ref = 3.42e-2  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
#     # m_ref = 1000#3.42  # (A/m2)(m3/mol)**1.5 - includes ref concentrations
#     # E_r = 17800
#     # arrhenius = pybamm.exp(E_r / pybamm.constants.R * (1 / 298.15 - 1 / T))

#     # return (
#     #     m_ref * arrhenius * c_e**0.5 * c_s_surf**0.5 * (c_s_max - c_s_surf) ** 0.5
#     # )
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


def get_parameter_values():

    return {
        #"chemistry": "lithium_ion",
        ################# sei
        "Primary: Ratio of lithium moles to SEI moles": 0.0,
        "Primary: Inner SEI partial molar volume [m3.mol-1]": 0.0,
        "Primary: Outer SEI partial molar volume [m3.mol-1]": 0.0,
        "Primary: SEI resistivity [Ohm.m]": 0.0,
        "Primary: Initial inner SEI thickness [m]": 0.0,
        "Primary: Initial outer SEI thickness [m]": 0.0,
        "Primary: EC initial concentration in electrolyte [mol.m-3]": 0.0,
        "Primary: EC diffusivity [m2.s-1]": 0.0,
        "Primary: SEI kinetic rate constant [m.s-1]": 0.0,
        "Primary: SEI open-circuit potential [V]": 0.0,
        "Primary: SEI growth activation energy [J.mol-1]": 0.0,
        "Secondary: Ratio of lithium moles to SEI moles": 0.0,
        "Secondary: Inner SEI partial molar volume [m3.mol-1]": 0.0,
        "Secondary: Outer SEI partial molar volume [m3.mol-1]": 0.0,
        "Secondary: SEI resistivity [Ohm.m]": 0.0,
        "Secondary: Initial inner SEI thickness [m]": 0.0,
        "Secondary: Initial outer SEI thickness [m]": 0.0,
        "Secondary: EC initial concentration in electrolyte [mol.m-3]": 0.0,
        "Secondary: EC diffusivity [m2.s-1]": 0.0,
        "Secondary: SEI kinetic rate constant [m.s-1]": 0.0,
        "Secondary: SEI open-circuit potential [V]": 0.0,
        "Secondary: SEI growth activation energy [J.mol-1]": 0.0,
#  # Primary active material is NCA
# # Secondary active material is LMO

        # Negative electrode
        "Negative current collector thickness [m]": 1.2e-05,
        "Negative electrode thickness [m]": 8.52e-05,
        "Separator thickness [m]": 1.2e-05,
        "Positive electrode thickness [m]": 7.56e-05,
        "Positive current collector thickness [m]": 1.6e-05,
        "Electrode height [m]": 0.065,
        "Electrode width [m]": 1.58,
        "Cell cooling surface area [m2]": 0.00531,
        "Cell volume [m3]": 2.42e-05,
        "Cell thermal expansion coefficient [m.K-1]": 1.1e-06,
        "Negative current collector conductivity [S.m-1]": 58411000.0,
        "Positive current collector conductivity [S.m-1]": 36914000.0,
        "Negative current collector density [kg.m-3]": 8960.0,
        "Positive current collector density [kg.m-3]": 2700.0,
        "Negative current collector specific heat capacity [J.kg-1.K-1]": 385.0,
        "Positive current collector specific heat capacity [J.kg-1.K-1]": 897.0,
        "Negative current collector thermal conductivity [W.m-1.K-1]": 401.0,
        "Positive current collector thermal conductivity [W.m-1.K-1]": 237.0,
        "Negative electrode conductivity [S.m-1]": 215.0,
        "Maximum concentration in negative electrode [mol.m-3]": 33133.0,
        "Negative electrode diffusivity [m2.s-1]": 3.3e-14,
        "Negative electrode OCP [V]": graphite_ocp_Enertech_Albertus2009,
        "Negative electrode porosity": 0.25,
        "Negative electrode active material volume fraction": 0.75,
        "Negative particle radius [m]": 5.86e-06,
        "Negative electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Negative electrode Bruggeman coefficient (electrode)": 0,
        "Negative electrode cation signed stoichiometry": -1.0,
        "Negative electrode electrons in reaction": 1.0,
        "Negative electrode charge transfer coefficient": 0.5,
        "Negative electrode double-layer capacity [F.m-2]": 0.2,
        "Negative electrode exchange-current density [A.m-2]"
        "": graphite_LGM50_electrolyte_exchange_current_density_Chen2020,
        "Negative electrode density [kg.m-3]": 1657.0,
        "Negative electrode specific heat capacity [J.kg-1.K-1]": 700.0,
        "Negative electrode thermal conductivity [W.m-1.K-1]": 1.7,
        "Negative electrode OCP entropic change [V.K-1]": 0.0,


        # Positive electrode
        "Positive electrode conductivity [S.m-1]": 215.0,
        "Primary: Maximum concentration in positive electrode [mol.m-3]": 24161.0,
        "Primary: Initial concentration in positive electrode [mol.m-3]": 9664.4,
        "Primary: Positive electrode diffusivity [m2.s-1]": nca_diffusivity_Albertus2009,
        "Primary: Positive electrode OCP [V]": nca_ocp_Albertus2009,
        "Positive electrode porosity": 0.25,
        "Primary: Positive electrode active material volume fraction": 0.3,
        "Primary: Positive particle radius [m]": 1.7e-06,
        "Positive electrode Bruggeman coefficient (electrolyte)": 1.5,
        "Positive electrode Bruggeman coefficient (electrode)": 0,
        "Positive electrode cation signed stoichiometry": -1.0,
        "Primary: Positive electrode electrons in reaction": 1.0,
        "Positive electrode charge transfer coefficient": 0.5,
        "Negative electrode double-layer capacity [F.m-2]": 0.2,
        "Primary: Positive electrode exchange-current density [A.m-2]"
        "": nca_electrolyte_exchange_current_density_Albertus2009,
        "Primary: Positive electrode density [kg.m-3]": 4100.0,
        "Positive electrode specific heat capacity [J.kg-1.K-1]": 700.0,
        "Positive electrode thermal conductivity [W.m-1.K-1]": 1.7,
        "Primary: Negative electrode OCP entropic change [V.K-1]": 0.0,
        "Secondary: Maximum concentration in positive electrode [mol.m-3]": 49459.0,
        "Secondary: Initial concentration in positive electrode [mol.m-3]": 18052.0,
        "Secondary: Positive electrode diffusivity [m2.s-1]": 2.5e-06,
        "Secondary: Positive electrode lithiation OCP [V]"
        "": lmo_ocp_lithiation_Albertus2009,
        "Secondary: Positive electrode delithiation OCP [V]"
        "": lmo_ocp_delithiation_Albertus2009,
        "Secondary: Positive electrode active material volume fraction": 0.3,
        "Secondary: Positive particle radius [m]": 2.5e-06,
        "Secondary: Positive electrode electrons in reaction": 1.0,
        "Secondary: Positive electrode exchange-current density [A.m-2]"
        "":lmo_electrolyte_exchange_current_density_Albertus2009,
        "Secondary: Positive electrode density [kg.m-3]": 4450.0,
        "Secondary: Positive electrode OCP entropic change [V.K-1]": 0.0,
        "Typical current [A]": 0.0021,
        "Current function [A]": 0.0021,
        "Contact resistance [Ohm]": 0.0,
    


        "Positive current collector thickness [m]": 1.6e-05,
        "Electrode height [m]": 1.407e-2,
        "Electrode width [m]": 1.407e-2,
        "Cell cooling surface area [m2]": 0.00531,
        "Cell volume [m3]": 99e-10,
        "Cell thermal expansion coefficient [m.K-1]": 1.1e-06,
        "Positive current collector conductivity [S.m-1]": 36914000.0,
        "Positive current collector density [kg.m-3]": 2700.0,
        "Positive current collector specific heat capacity [J.kg-1.K-1]": 897.0,
        "Positive current collector thermal conductivity [W.m-1.K-1]": 237.0,
        'Nominal cell capacity [A.h]': 0.0021,
        #         ############ separator
        #"Separator porosity": 0.0,
        #"Separator Bruggeman coefficient (electrolyte)": 0.0,
        #"Separator density [kg.m-3]": 0.0,
        #"Separator specific heat capacity [J.kg-1.K-1]": 0.0,
        #"Separator thermal conductivity [W.m-1.K-1]": 0.0,
        "Separator porosity": 0.47,
        "Separator Bruggeman coefficient (electrolyte)": 1.5,
        "Separator density [kg.m-3]": 397.0,
        "Separator specific heat capacity [J.kg-1.K-1]": 700.0,
        "Separator thermal conductivity [W.m-1.K-1]": 0.16,
        
        
        ############ electrolyte
        "Typical electrolyte concentration [mol.m-3]": 1000.0,
        "Initial concentration in electrolyte [mol.m-3]": 1000.0,
        "Cation transference number": 0.37,
        "1 + dlnf/dlnc": 1.0,
        "Electrolyte diffusivity [m2.s-1]": electrolyte_diffusivity_Albertus2009,
        "Electrolyte conductivity [S.m-1]": electrolyte_conductivity_Albertus2009,
#         ############ experiment
        "Reference temperature [K]": 298.15,
        "Total heat transfer coefficient [W.m-2.K-1]": 10.0,
        "Ambient temperature [K]": 298.15,
        "Number of electrodes connected in parallel to make a cell": 1.0,
        "Number of cells connected in series to make a battery": 1.0,
        "Lower voltage cut-off [V]": 3,
        "Upper voltage cut-off [V]": 4.2,
        "Initial concentration in positive electrode [mol.m-3]": 2000000.0,
        "Initial temperature [K]": 298.15,
    }



       

#         ############# negative electrode
#         # 'Negative electrode conductivity [S.m-1]': 10.0,
#         # "Primary: Maximum concentration in negative electrode [mol.m-3]":24161.0,
#         # "Primary: Initial concentration in negative electrode [mol.m-3]":9664.4,
#         # "Primary: Negative electrode diffusivity [m2.s-1]":6.0e-15,

#         "Primary: Maximum concentration in Positive electrode [mol.m-3]":24161.0,
#         "Primary: Initial concentration in Positive electrode [mol.m-3]":9664.4,
#         "Primary: Positive electrode diffusivity [m2.s-1]":nca_diffusivity,
  

#         #"Primary: Negative electrode OCP [V]": nca_ocp,
#         "Primary: Positive electrode OCP [V]": graphite_ocp_Enertech,
#         "Positive electrode OCP [V]": graphite_ocp_Enertech,

#         "Positive electrode porosity": 0.25,
#         'Primary: Negative electrode active material volume fraction': 0.3,
#         'Primary: Negative particle radius [m]': 1.7e-06,
#         "Negative electrode Bruggeman coefficient (electrolyte)": 1.5,
#         "Negative electrode Bruggeman coefficient (electrode)": 0,
     
#         # ############### positive electrode
#         # 'Positive electrode conductivity [S.m-1]': 10.0,
#         # "Primary: Maximum concentration in positive electrode [mol.m-3]":24161.0,
#         # "Primary: Initial concentration in positive electrode [mol.m-3]":9664.4,
#         # "Primary: Positive electrode diffusivity [m2.s-1]":6.0e-15,
#         # #"Primary: Positive electrode OCP [V]": nca_ocp,
#         # "Primary: Positive electrode OCP [V]": nca_ocp_Albertus2009,
#         # "Positive electrode porosity": 0.25,
#         # 'Primary: Positive electrode active material volume fraction': 0.3,
#         # 'Primary: Positive particle radius [m]': 1.7e-06,
#         # "Positive electrode Bruggeman coefficient (electrolyte)": 1.5,
#         # "Positive electrode Bruggeman coefficient (electrode)": 0,
#         # "Positive electrode cation signed stoichiometry": -1.0,
#         # "Primary: Positive electrode electrons in reaction": 1.0,
#         # "Positive electrode charge transfer coefficient": 0.5,
#         # "Positive electrode double-layer capacity [F.m-2]": 0.2,
#         # "Primary: Positive electrode exchange-current density [A.m-2]"
#         # "": nca_electrolyte_exchange_current_density,
#         # 'Primary: Positive electrode density [kg.m-3]': 4100.0,
#         # "Positive electrode specific heat capacity [J.kg-1.K-1]": 700.0,
#         # "Positive electrode thermal conductivity [W.m-1.K-1]": 1.7,
#         # "Primary: Positive electrode OCP entropic change [V.K-1]": 0.0,
#         # "Secondary: Maximum concentration in positive electrode [mol.m-3]":49459.0,
#         # "Secondary: Initial concentration in positive electrode [mol.m-3]":18052.5, 
#         # "Secondary: Positive electrode diffusivity [m2.s-1]":3.0e-15,
#         # #"Secondary: Positive electrode diffusivity [m2.s-1]":nca_diffusivity,
#         # "Secondary: Positive electrode lithiation OCP [V]"
#         # "": lmo_ocp_lithiation,
#         # "Secondary: Positive electrode delithiation OCP [V]"
#         # "": lmo_ocp_delithiation,
#         # 'Secondary: Positive electrode active material volume fraction': 0.3,  
#         # 'Secondary: Positive particle radius [m]': 2.5e-06,
#         # "Secondary: Positive electrode electrons in reaction": 1.0,
#         # "Secondary: Positive electrode exchange-current density [A.m-2]"
#         # "": lmo_electrolyte_exchange_current_density,
#         # 'Secondary: Positive electrode density [kg.m-3]': 4450.0,
#         # "Secondary: Positive electrode OCP entropic change [V.K-1]": 0.0,




#         # "Positive electrode conductivity [S.m-1]":1000.000,
#         # "Maximum concentration in positive electrode [mol.m-3]": 5000000.0,#631040.0,
#         # "Positive electrode diffusivity [m2.s-1]":1,
#         # "Positive electrode OCP [V]": nmc_LGM50_ocp_Chen2020,
#         # #"Positive electrode OCP [V]": 3,
#         # "Positive electrode porosity": 0.335,
#         # "Positive electrode active material volume fraction": 0.665,
#         # "Positive particle radius [m]": 5.22e-06,
#         # "Positive electrode Bruggeman coefficient (electrolyte)": 1.5,
#         # "Positive electrode Bruggeman coefficient (electrode)": 0,
#         # "Positive electrode cation signed stoichiometry": -1.0,
#         # "Positive electrode electrons in reaction": 1.0,
#         # "Positive electrode charge transfer coefficient": 0.5,
#         # "Positive electrode double-layer capacity [F.m-2]": 0.2,
#         # "Positive electrode exchange-current density [A.m-2]"
#         # "": 1000.0,#nmc_LGM50_electrolyte_exchange_current_density_Chen2020,
#         # "Positive electrode density [kg.m-3]": 3262.0,
#         # "Positive electrode specific heat capacity [J.kg-1.K-1]": 700.0,
#         # "Positive electrode thermal conductivity [W.m-1.K-1]": 2.1,
#         # "Positive electrode OCP entropic change [V.K-1]": 0.0,
        
#         ############ separator
#         #"Separator porosity": 0.0,
#         #"Separator Bruggeman coefficient (electrolyte)": 0.0,
#         #"Separator density [kg.m-3]": 0.0,
#         #"Separator specific heat capacity [J.kg-1.K-1]": 0.0,
#         #"Separator thermal conductivity [W.m-1.K-1]": 0.0,
#         "Separator porosity": 0.47,
#         "Separator Bruggeman coefficient (electrolyte)": 1.5,
#         "Separator density [kg.m-3]": 397.0,
#         "Separator specific heat capacity [J.kg-1.K-1]": 700.0,
#         "Separator thermal conductivity [W.m-1.K-1]": 0.16,
        
        
#         ############ electrolyte
#         "Typical electrolyte concentration [mol.m-3]": 1000.0,
#         "Initial concentration in electrolyte [mol.m-3]": 1000.0,
#         "Cation transference number": 0.37,
#         "1 + dlnf/dlnc": 1.0,
#         "Electrolyte diffusivity [m2.s-1]": electrolyte_diffusivity,
#         "Electrolyte conductivity [S.m-1]": electrolyte_conductivity,
#         ############ experiment
#         "Reference temperature [K]": 298.15,
#         "Total heat transfer coefficient [W.m-2.K-1]": 10.0,
#         "Ambient temperature [K]": 298.15,
#         "Number of electrodes connected in parallel to make a cell": 1.0,
#         "Number of cells connected in series to make a battery": 1.0,
#         "Lower voltage cut-off [V]": -0.1,
#         "Upper voltage cut-off [V]":- 0.8,
#         "Initial concentration in negative electrode [mol.m-3]": 27716.9,
#         "Initial concentration in positive electrode [mol.m-3]": 2000000.0,
#         "Initial temperature [K]": 298.15,
    


