class TrigPy:

    def calc_angle(AB, BC):#, G, RT
        from math import atan2, degrees

        if AB>0 and BC>0:
            return str(round(degrees(atan2(abs(AB), abs(BC))))) + '°'
        elif AB>0 and BC<0:
            return str(round(180-degrees(atan2(abs(AB), abs(BC))))) + '°'   
        elif AB<0 and BC<0:
            return str(round(180+degrees(atan2(abs(AB), abs(BC))))) + '°'
        elif AB<0 and BC>0:
            return str(round(360-degrees(atan2(abs(AB), abs(BC))))) + '°'
        elif AB==0 and BC>0:
            return str(90) + '°'
        elif AB<0 and BC==0:
            return str(180) + '°'
        elif AB==0 and BC<0:
            return str(270) + '°'
        elif AB>0 and BC==0:
            return str(0) + '°'