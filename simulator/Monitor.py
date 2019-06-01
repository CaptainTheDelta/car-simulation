# coding: utf-8
from simulator.__init__ import *



class Monitor():
    """Détecteur de bouchons."""
    def __init__(self,road):
        """Initialise le surveillant.

        Args:
            road (Road): Route à surveiller.
        """
        self.road = road
        self.L = road.get_length()

        self.TJs = []
        self.SDs = []

        self.m = 0
        self.nm = 0

    def find_traffic_problems(self):
        """Renvoie une liste de ralentissements et d'embouteillage.

        Return:
            (list): Ralentissements ou embouteillages.
        """
        status = self.road.get_current_status()
        cars = [(o,p) for (o,p) in status if type(o) == Car]

        movingCars = []
        notMovingCars = []

        for (car,p) in cars:
            if car.get_speed() > 10:
                movingCars.append((car,p))
            else:
                notMovingCars.append((car,p))

        pbms = []

        def detect(cars,obj):
            n = len(cars)
            i = 0
            lObj = []

            while i < n:
                pos = cars[i][1]
                x = pos

                while i < n-1 and cars[i+1][1] < x + SAFETY_DISTANCE*1.2:
                    x = cars[i+1][1]
                    i += 1
                
                if x != pos:
                    lObj.append(obj(pos,x-pos))
                    # if type(obj) == TrafficJam:
                    #     log.debug(f"Ralentissement : {pos}")
                    # else:
                    #     log.debug(f"Embouteillage : {pos}")
                i += 1

            return lObj

        m = detect(movingCars,Slowdown)
        nm = detect(notMovingCars,TrafficJam)
        pbms.extend(m)
        pbms.extend(nm)
        
        # if self.m != len(m) or self.nm != len(nm):
        #     log.debug(f"{len(m)} ralentissement{s(len(m))}  \t{len(nm)} embouteillage{s(len(nm))}")
        #     self.m = len(m)
        #     self.nm = len(nm)

        return pbms


log.debug(f"{__name__} importé.")