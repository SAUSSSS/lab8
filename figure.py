import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
nx = 50 
nt = 40 
dx = 1/nx
dt = 0.01/nt
u, v = np.mgrid[0:1:dx, 0:0.005:dt]
x = u
y = v

z = np.exp(-4.0 * np.pi * np.pi * y) * np.sin(2.0*np.pi * x)
fig = plt.figure()


ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='inferno')


