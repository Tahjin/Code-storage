from matplotlib import pyplot as plt
import numpy as np
# from TrigPy import TrigPy
import random

z=[]
x=[]
y=[]
random.seed(5)
epochs=4 
for i in range(epochs):
    
    x.append(random.randint(1, 35))
random.seed(4) 
for i in range(epochs):
    
    y.append(random.randint(1, 35))
random.seed(10) 
for i in range(epochs):
    
    z.append(random.randint(1, 35))
# plt.rcParams['figure.figsize']=(8,6)
fig = plt.figure(figsize = (8, 6))

ax = plt.axes(projection='3d')

ax.plot3D(x,y,z)
ax.scatter3D(x, y, z, c='green', cmap='cividis', s=100)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

for i in range(len(x)):
    print("Point: "+str(x[i])+","+str(y[i])+","+str(z[i]))

#notes
#that that we have everything for the graph ready next part is pulling data out of the points
#like what is the change of distance between points as well as change
#In axis, do fractals emerge.
ax.view_init(90,90)
plt.show()
