from matplotlib import pyplot as plt
#
#
x = [15,40,24,12]
y = [9,32,13,60]
test1=[0,100]
test2=[0,100]
plt.plot(test1,test2)
  
for i in range(len(x)):
    # x.append(i)
    # y.append(i)

    # Mention x and y limits to define their range
    plt.xlim(0, 100)
    plt.ylim(0, 100)

    # Ploting graph     
    if i!=len(x):
        plt.plot(x[0:i+1], y[0:i+1], color = 'green')             
    else:
        plt.plot(x, y, color = 'green')   

      

    
    plt.pause(1)
  
plt.show()