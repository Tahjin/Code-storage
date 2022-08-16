import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import random
reg=LinearRegression()

xval=[]
yval=[]

for i in range(4):#contols number of iterations
    plt.clf()
    xval.append(random.randint(0,100))
    yval.append(random.randint(0,100))

    x=np.array(xval)
    x=x.reshape(-1,1)

    y=np.array(yval)
    y=y.reshape(-1,1)

    reg.fit(x,y)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.scatter(xval,yval,color="green")
    plt.plot(x,y)
    plt.pause(0.001)

plt.show()