import random
import matplotlib.pyplot as plt

SQN=[17, 23, 34, 2, 30, 16, 4, 11, 8, 24]#sequnce starting numbers


random.seed(5)
epochs=50000000
SQcount=0
numlist=[]

# for i in range(epochs):

#     num=random.randint(1, 35)

#     if SQcount==6:
#         print(i-6)
#         SQcount=0
#     elif num==SQN[SQcount]:
#         SQcount+=1
#     else:
#         SQcount=0

####
for i in range(epochs):

    num=random.randint(1, 35)
    numlist.append(num)

test=39793056
j=0
for i in range(10):
    print(numlist[test+j])
    j+=1

