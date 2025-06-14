import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def init():
    line.set_data([], [])
    return line,

def animate(j):
    line.set_data(o, final_densite[j,:]) #Crée un graphique pour chaque densite sauvegarde
    return line,

HBAR = 1.054571818e-34
ME = 9.1093897e-31
L = 0.1
E0 = HBAR**2 * math.pi ** 2 / 2 / ME / L**2

dt=1E-7
dx=0.001
nx=int(1/dx)*2
nt=90000 # En fonction du potentiel il faut modifier ce parametre car sur certaines animations la particule atteins les bords
nd=int(nt/1000)+1#nombre d image dans notre animation
n_frame = nd
s=dt/(dx**2)
xc=0.6
sigma=0.05
A=1/(math.sqrt(sigma*math.sqrt(math.pi)))
v0=1000
e=E0/v0 - 1#Valeur du rapport E/V0
E=e*v0
k=math.sqrt(2*abs(E))

o=np.zeros(nx)
V=np.zeros(nx)

# Initialisation des tableaux
o = np.linspace(0, (nx - 1) * dx, nx)
V = np.zeros(nx)
V[(o >= 0.8) & (o<=0.9)] = -v0  # Potentiel

cpt = A * np.exp(1j * k * o - ((o - xc) ** 2) / (2 * (sigma ** 2)))
densite=np.zeros((nt,nx))
densite[0,:] = np.absolute(cpt[:]) ** 2
final_densite=np.zeros((n_frame,nx))
re=np.zeros(nx)
re[:]=np.real(cpt[:])

b=np.zeros(nx)

im=np.zeros(nx)
im[:]=np.imag(cpt[:])

it=0
for i in range(1, nt):
    if i % 2 != 0:
        b[1:-1]=im[1:-1]
        im[1:-1] = im[1:-1] + s * (re[2:] + re[:-2]) - 2 * re[1:-1] * (s + V[1:-1] * dt)
        densite[i,1:-1] = re[1:-1]*re[1:-1] + im[1:-1]*b[1:-1]
    else:
        re[1:-1] = re[1:-1] - s * (im[2:] + im[:-2]) + 2 * im[1:-1] * (s + V[1:-1] * dt)

for i in range(1,nt):
    if((i-1)%1000==0):
        it+=1
        final_densite[it][:]=densite[i][:]

plot_title = "Marche Ascendante avec E/Vo="+str(e)

fig = plt.figure() # initialise la figure principale
line, = plt.plot([], [])
plt.ylim(-5,13)
plt.xlim(0,2)
plt.plot(o,V,label="Potentiel")
plt.title(plot_title)
plt.xlabel("x")
plt.ylabel("Densité de probabilité de présence")
plt.legend() #Permet de faire apparaitre la legende

ani = animation.FuncAnimation(fig,animate,init_func=init, frames=nd, blit=False, interval=100, repeat=False)
#file_name = 'paquet_onde_e='+str(e)+'.mp4'
#ani.save(file_name, writer = animation.FFMpegWriter(fps=120, bitrate=5000))
plt.show()
