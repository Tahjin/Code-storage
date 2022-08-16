#point (10,4)
#point (5,5)
#point (12,2)
#point (6,12)
import math 
import numpy as np

# print(np.arctan(6/8))
#calc_angle(run,rise)
#useing the rise over run between two points 
def calc_angle(AB, BC):#, G, RT
    from math import atan2, degrees

    if AB>0 and BC>0:
        print(str(round(degrees(atan2(abs(AB), abs(BC))))) + '°')
    elif AB>0 and BC<0:
        print(str(round(180-degrees(atan2(abs(AB), abs(BC))))) + '°')   
    elif AB<0 and BC<0:
        print(str(round(180+degrees(atan2(abs(AB), abs(BC))))) + '°')
    elif AB<0 and BC>0:
        print(str(round(360-degrees(atan2(abs(AB), abs(BC))))) + '°')
    elif AB==0 and BC>0:
        print(str(90) + '°')
    elif AB<0 and BC==0:
        print(str(180) + '°')
    elif AB==0 and BC<0:
        print(str(270) + '°')
    elif AB>0 and BC==0:
        print(str(0) + '°')

calc_angle(1,-5)
