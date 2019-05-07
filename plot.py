import numpy as np
from matplotlib import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

nx=101
nt=300
DATOS = np.loadtxt("Archivo.dat")
MALLADO = np.reshape(DATOS, (nx, nt))

l=10.
t=6.
dx=l/nx

X_=[]
Y_0=[]
Y_F=[]
# SE inicializar el grid para graficar
t1 = np.linspace(0, t, nt)
l1 = np.linspace(0, l, nx)
ll, tt = np.meshgrid(t1, l1)

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.set_xlabel('T(s)')
ax1.set_ylabel('X(metros)')
ax1.set_zlabel('Desplazamiento(metros)')
surf = ax1.plot_surface(ll, tt, MALLADO,cmap=cm.coolwarm)

#Poner la barra de calor

fig1.colorbar(surf, shrink=0.9, aspect=4.5)
plt.savefig("plot_3d.png")


plt.figure()

#Grafica de configuracion incial y final

for ix in range(nx):
    X_.append(dx*ix)
    Y_0.append(MALLADO[ix][0])
    Y_F.append(MALLADO[ix][nt-1])

plt.plot(X_,Y_0)
plt.plot(X_,Y_F)
plt.xlabel("X(metros)")
plt.ylabel("Desplazamiento(metros)")

plt.gca().legend(('Conf inicial','Config final'))
plt.savefig("plot_simple.png")



