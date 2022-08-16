import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
reg=LinearRegression()


xval=[50,13,70,10]
yval=[10,30,50,60]


for i in range(len(xval)):#contols number of iterations
    plt.clf()

    if i!=len(xval):
        xAn=np.array(xval[0:i+1])  
        yAn=np.array(yval[0:i+1])              
    else:
        xAn=np.array(xval)  
        yAn=np.array(yval) 

    xAn=xAn.reshape(-1,1)
    yAn=yAn.reshape(-1,1)

    reg.fit(xAn,yAn)
    plt.xlim(0,100)
    plt.ylim(0,100)
    plt.scatter(xval,yval,color="green")
    plt.plot(xAn,yAn)
    plt.pause(1)
test1=[0,100]
test2=[0,100]
plt.plot(test1,test2)
plt.show()