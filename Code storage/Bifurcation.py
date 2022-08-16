import matplotlib.pyplot as plt
import numpy as np

R=np.linspace(2.5,4,10000)

print(R)
X=[]
Y=[]

for r in R:
    X.append(r)

    x=np.random.random()
    for n in range(100):#ignores transient effect?
        x=r*x*(1-x)

    for n in range(100):
        x=r*x*(1-x)
    Y.append(x)

# oh so in a way x and y are kinda the same 
# graph but compared
plt.plot(X,Y,ls='',marker=',')
plt.show()

