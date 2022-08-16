from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x/2)+5

fig, ax = plt.subplots()
ax.set_xlim(0,10)
ax.set_ylim(0,10)
ax.set_xlabel("X-axsis")
ax.set_ylabel("Y-axsis")

secondline=[]
for x in np.arange(20):
    secondline.append(f(x))

ax.plot(np.arange(20),np.arange(20))#we can replace these with list of numbers if need be
ax.plot(np.arange(20),secondline)

num_iter=10
x_0=1
pointlist=[]
pointlist.append((x_0,0))
for i in range(num_iter):
    x, y = pointlist[-1]
    y=f(x)
    pointlist.append((x,y))
    x=y
    pointlist.append((x,y))   
point_array=np.array(pointlist)
X,Y=point_array.T

def animateG(xlist,ylist):
    for i in range(len(xlist)):#contols number of iterations
        plt.clf()

        if i!=len(xlist):
            xAn=np.array(xlist[0:i+1])  
            yAn=np.array(ylist[0:i+1])              
        else:
            xAn=np.array(xlist)  
            yAn=np.array(ylist) 

        xAn=xAn.reshape(-1,1)
        yAn=yAn.reshape(-1,1)#

        # reg.fit(xAn,yAn)

        ax.plot(xAn,yAn)

# animateG(X,Y)
ax.plot(X,Y)
plt.show()