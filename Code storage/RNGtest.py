import random
import matplotlib.pyplot as plt

x=[]
num=[]
time=[]
line=0

random.seed(5)
epochs=500
for i in range(epochs):
    
    x.append(random.randint(1, 35))

for t in range(len(x)):
    time.append(t)
    if x[t]==x[0]:
        line=x[t]
        num.append(line)
    elif x[t]>x[t-1]:
        line+=x[t]
        num.append(line)
    elif x[t]<x[t-1]:
        line-=x[t-1]-x[t]
        num.append(line)
    else:
        num.append(line)



plt.plot(time,num)
# print(num[40])
plt.show()
# controlnum=x[0]
# for i in range(len(x)):
#     if x[i]==controlnum:
#         print("Point "+str(i)+":  "+str(x[i]))
#     else:
#         continue

