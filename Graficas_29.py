import numpy as np
from matplotlib import pylab as pl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm

nx=101
nt=300

l=1.
t=6.
dx=l/nx

X_=[]
Y_0=[]
Y_F=[]

data = np.loadtxt("Archivo.dat")
grid = np.reshape(data, (nx, nt))

x1 = np.linspace(0, t, nt)
y1 = np.linspace(0, l, nx)
xx, yy = np.meshgrid(x1, y1)

fig1 = plt.figure()
ax1 = fig1.gca(projection='3d')
ax1.set_xlabel('Tiempo')
ax1.set_ylabel('Posicion')
ax1.set_zlabel('Desplazamiento')
surf = ax1.plot_surface(xx, yy, grid,cmap=cm.coolwarm)

fig1.colorbar(surf, shrink=0.5, aspect=5)
plt.savefig("plot_3d.png")

for ix in range(nx):
    X_.append(dx*ix)
    Y_0.append(grid[ix][0])
    Y_F.append(grid[ix][nt-1])

plt.figure()
plt.plot(X_,Y_0)
plt.plot(X_,Y_F)
plt.gca().legend(('Tiempo inicial','Tiempo final'))
plt.xlabel("Posicion")
plt.ylabel("Desplazamiento")
plt.savefig("plot_simple.png")



