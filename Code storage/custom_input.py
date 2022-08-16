import pyinputplus as pyip
#range(len(numbersList))
def addsUpToTen(numbers):
    numbersList = list(numbers)
    print(numbersList)
#    for i, digit in enumerate(numbersList):#double varibles in loop
#        numbersList[i] = int(digit)
    if sum(int(numbersList)) != 10:
        raise Exception('The digits must add up to 10, not %s.' %
        (sum(int(numbersList)))
    
    return int(numbers) # Return an int form of numbers.

while True:
    print('\n')
    response = pyip.inputCustom(addsUpToTen) # No parentheses after