from matplotlib import pyplot as plt
import numpy as np

z=[0,10,21]
x=[0,10,25]
y=[0,10,14]
# plt.rcParams['figure.figsize']=(8,6)
fig = plt.figure(figsize = (8, 6))

ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)
ax.scatter3D(x, y, z, c='black', cmap='cividis', s=100)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# ax.view_init(0,0)
plt.show()
