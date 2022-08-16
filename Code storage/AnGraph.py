import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
reg=LinearRegression()

class AnGraph:

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

            reg.fit(xAn,yAn)
            # plt.xlim(0,framesize)
            # plt.ylim(0,framesize)
            # plt.scatter(xlist,ylist,color="green")
            plt.plot(xAn,yAn)
            plt.pause(1)

        plt.show()