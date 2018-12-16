# coding: utf-8
from .__init__ import *



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
                l = cars[i][0].get_length()
                x = pos + l

                while i < n-1 and cars[i+1][1] < x + SAFETY_DISTANCE*1.3:
                    x = cars[i+1][1] + cars[i+1][0].get_length()
                    i += 1
                
                if x != pos + l:
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
        
        if self.m != len(m) or self.nm != len(nm):
            log.debug(f"{len(m)} ralentissement{s(len(m))}  \t{len(nm)} embouteillage{s(len(nm))}")
            self.m = len(m)
            self.nm = len(nm)

        return pbms




class TrafficJam(OnTheRoad):
    """Embouteillage autoroutier."""
    def __init__(self,pos,length):
        """Initialise un embouteillage.

        Args:
            pos (float): Position de l'obstacle.
            length (float): Longueur de l'embouteillage.
        """
        super().__init__(pos,length,1,red)

    def update(self,pos,l):
        """Modifie la position et la longueur de l'embouteillage.

        Args:
            pos (float): Nouvelle position.
            l (float): Nouvelle longueur.
        """
        self.pos = pos
        self.l = l

    def draw(self,contener,l):
        """Dessine l'object sur la route.

        Args:
            contener (pygame.?): Conteneur.
            l (int): Ligne centrale de la route.
        """
        x = int(self.pos)
        y = l - int(self.w/2)
        l = int(self.l)
        w = int(self.w)

        pygame.draw.rect(contener, self.color, (x,y,l,w))



class Slowdown(OnTheRoad):
    """Ralentissement. Encore un papy."""
    def __init__(self,pos,length):
        """Initialise un ralentissement.

        Args:
            pos (float): Position de l'obstacle.
            length (float): Longueur du ralentissement.
        """
        super().__init__(pos,length,1,orange)

    def update(self,pos,l):
        """Modifie la position et la longueur du ralentissement.

        Args:
            pos (float): Nouvelle position.
            l (float): Nouvelle longueur.
        """
        self.pos = pos
        self.l = l

log.debug(f"{__name__} importé.")