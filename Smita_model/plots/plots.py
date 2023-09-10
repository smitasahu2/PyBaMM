import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')

def ua(x):
  # U_eq in Anode
  a = 1.9793
  b = 39.028
  c = 0.2482
  d = 0.0909
  e = 29.8538
  g = 0.1234
  h = 0.04478
  i = 14.9159
  j = 0.2769
  k = 0.0205
  m = 30.4444
  n = 0.6103
  y = a * np.exp(-b * x) + c - d * np.tanh(e * (x - g)) - h* np.tanh(i* (x - j)) - k * np.tanh(m * (x - n))
  return y;


def dua(x):
# Derivative of U_eq in Anode
  a = 1.9793
  b = 39.028
  c = 0.2482
  d = 0.0909
  e = 29.8538
  g = 0.1234
  h = 0.04478
  i1 = 14.9159
  j1 = 0.2769
  k1 = 0.0205
  m = 30.4444
  n = 0.6103
  y = -a * b * np.exp(-b * x) - d * e * (1 - np.tanh(e * (x - g))**2) - h * i1 * (1 - np.tanh(i1 * (x - j1))**2)- k1 * m * (1 - np.tanh(m * (x - n))**2)
  y = y / 33133; 
  return y;


def iua(x):
# Integral of U_eq in Anode
  a = 1.9793
  b = 39.028
  c = 0.2482
  d = 0.0909
  e = 29.8538
  g = 0.1234
  h = 0.04478
  i1 = 14.9159
  j1 = 0.2769
  k = 0.0205
  m = 30.4444
  n = 0.6203
  y = -a/b * np.exp(-b * x) + c * x + d/e * np.log(np.cosh(e * (x - g))) + h/i1 * np.log(np.cosh(i1 * (x - j1))) + k/m * np.log(np.cosh(m * (x - n)))
  y = y * 33133.0 
  return y;
x = np.linspace(0, 1, 1000)




def uc(x):
  # U_eq in Cathode
  a = -0.8090
  c = 4.4875
  d = 0.0428
  e = 18.5138
  g = 0.5542
  h = 17.7326
  i = 15.7890
  j = 0.3117
  k = 17.5842
  m = 15.9308
  n = 0.3120

  y = a * x + c - d * np.tanh(e * (x - g)) - h * np.tanh(i * (x - j)) + k * np.tanh(m * (x - n));
  return y 





def duc(x):
  # Derivative of U_eq in Cathode

  a = -0.8090
  c = 4.4875
  d = 0.0428
  e = 18.5138
  g = 0.5542
  h = 17.7326
  i = 15.7890
  j = 0.3117
  k = 17.5842
  m = 15.9308
  n = 0.3120
    
  y= a - d*e*(1 - np.tanh(e*(x-g))**2) - h*i*(1 - np.tanh(i*(x-j))**2) + k*m*(1 - np.tanh(m*(x-n))**2)
    
  y = y / 63104.0;
  return y

def iuc(x):
  # Integral of U_eq in Cathode
  a = -0.8090
  c = 4.4875
  d = 0.0428
  e = 18.5138
  g = 0.5542
  h = 17.7326
  i = 15.7890
  j = 0.3117
  k = 17.5842
  m = 15.9308
  n = 0.3120
    
  y = (a/2)*x**2 + c*x + d/e*np.log(np.cosh(e*(x-g))) + h/i*np.log(np.cosh(i*(x-j))) - k/m*np.log(np.cosh(m*(x-n)));
  y = y * 63104.0;
  
  return y


def Da(x):
  return 3.3e-10 * np.ones_like(x)

def Dc(x):
  return  4e-11 * np.ones_like(x);




def kappa(cm):
  # Conductivity in the electrolyte
  return 0.1297 * cm * cm * cm - 2.51 * cm * np.sqrt(cm) + 3.329 * cm   # sqrt function from numpy module

def D(cm):
  # Diffusivity in the electrolyte
  # cm[0] = 1.0  # Avoid division by 0
  # De = 8.794e-11 * cm * cm  - 3.972e-10 * cm + 4.862e-10 #2.646e-6 * kappa / cm
  # De[0] = 2 * De[1] - De[2]  # Linear extrapolation
  # cm[0] = 0
   return 8.794e-11 * cm * cm  - 3.972e-10 * cm + 4.862e-10


fig, ax = plt.subplots(2, 4, figsize=(12, 4))
ax[0,0].plot(x, ua(x))
ax[0,0].set(xlabel="sto [-]", ylabel="$U^a_eq$ [V]")
ax[0,1].plot(x, dua(x))
ax[0,1].set(xlabel="sto [-]", ylabel="$dU^a_eq$ [V/m]")
ax[0,2].plot(x, iua(x))
ax[0,2].set(xlabel="sto [-]", ylabel="$\int_0^xU^a_{eq} dx$ [V m]")
ax[0,3].plot(x, Da(x))
ax[0,3].set(xlabel="sto [-]", ylabel="$Da$ [cm$^2$/s]")
ax[1,0].plot(x, uc(x))
ax[1,0].set(xlabel="sto [-]", ylabel="$U^c_{eq}$ [V]")
ax[1,1].plot(x, duc(x))
ax[1,1].set(xlabel="sto [-]", ylabel="$dU^c_{eq}$ [V/m]")
ax[1,2].plot(x, iuc(x))
ax[1,2].set(xlabel="sto [-]", ylabel="$\int_0^xU^c_{eq} dx$ [V m]")
ax[1,3].plot(x, Dc(x))
ax[1,3].set(xlabel="sto [-]", ylabel="$Dc$ [cm$^2$/s]")
plt.tight_layout()
plt.show()
# fig.suptitle('le', fontsize=16)

cm = np.linspace(0, 2, 100)

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].plot(cm, kappa(cm))
ax[0].set(xlabel="sto [-]", ylabel="$\kappa$ [A/m/V]")
ax[1].plot(cm, D(cm))
ax[1].set(xlabel="sto [-]", ylabel="$D$ [m$^2$/s]")
plt.tight_layout()
plt.show()

