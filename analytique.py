import numpy as np
import math
import matplotlib.pyplot as plt

# Exemple analytique du coefficient de transmission T

startx = 0.1
endx = 20

HBAR = 1.054571818e-34
M = 9.10938356e-31
L = 1e-18
E0 = HBAR**2 * math.pi ** 2 / 2 / M / L**2

dx=1e-3
nx=int((endx-startx)/dx)
v0=5
E=np.zeros(nx)
T=np.zeros(nx)

# Initialisation des tableaux
E = np.linspace(startx, (nx - 1) * dx, nx)
k = np.sqrt(2*M*E)/HBAR
q = np.sqrt(2*M*(E+v0))/HBAR
T = 4*k*k*q*q/(4*k*k*q*q+(k*k-q*q)*(k*k-q*q)*np.sin(q*L)**2)

plot_title = "Coefficient de transmission en fonction de l'énergie"

fig = plt.figure() # initialise la figure principale
line, = plt.plot([], [])
plt.ylim(0,1.1)
plt.xlim(startx,endx)
plt.plot(E,T,label="Coeff de transmission")
plt.title(plot_title)
plt.xlabel("E")
plt.ylabel("T")
plt.legend() #Permet de faire apparaitre la legende

plt.show()