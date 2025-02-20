# coding: utf-8
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import matplotlib.pyplot as plt
import geometry

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

borders = geometry.getBorders()
surface = geometry.getSurface()

ax.scatter(*surface.T)
plt.show()
