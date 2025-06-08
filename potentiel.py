import numpy as np
import math
import matplotlib.pyplot as plt

# Affiche un exemple de puits de potentiel

startx = -1
endx = 2

dx=0.001
nx=int(1/dx)*(endx-startx)
v0=-10
E0 = 5

o=np.zeros(nx)
V=np.zeros(nx)

# Initialisation des tableaux
o = np.linspace(startx, (nx - 1) * dx, nx)
V = np.zeros(nx)
E = np.zeros(nx)
V[(o >= 0) & (o<=1)] = v0  # Potentiel
E[(o >= startx) & (o<=endx)] = E0  # Energie

plot_title = "Exemple de puits de potentiel avec V0 = 10 et E = 5"

fig = plt.figure() # initialise la figure principale
line, = plt.plot([], [])
plt.ylim(-12,8)
plt.xlim(startx,endx)
plt.plot(o,V,label="Potentiel")
plt.plot(o,E,label="Energie")
plt.title(plot_title)
plt.xlabel("x")
plt.ylabel("V")
plt.legend() #Permet de faire apparaitre la legende

plt.show()