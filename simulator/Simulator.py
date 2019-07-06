# coding: utf-8
from simulator.__init__ import *



class Simulator():
    """Simulateur."""

    def __init__(self,road_length,max_speed,spawn_proba,wait=False):
        """Initialise la simulation.

        Args:
            road_length (float): Longueur de la route.
            max_speed (float): Vitesse maximale autorisée sur la route.
                (à noter que certains conducteurs peuvent la dépasser...)
            spawn_proba (float): Probabilité qu'une voiture entre sur la route
                à chaque instant. (compris entre 0 et 1).
            wait (bool): Démarage immédiat de la simulation, ou pas.
        """
        self.road = Road("Voie 1",road_length,max_speed,spawn_proba)
        self.monitor = Monitor(self.road)
        
        self.D = []
        self.F = []

        if wait:
            for i in range(3,0,-1):
                log.info(i)
                sleep(1)


        # log.info("Action !")



    def get_res(self):
        k = 0
        n = len(self.D)
        d = 0
        f = 0

        while k < n and self.D[k] == 0 and self.F[k] == 0:
            k += 1

        if k != n:
            d = sum(self.D[k:]) / (n-k)
            f = sum(self.F[k:]) / (n-k)
        
        return d, f


    def update(self,n):
        d,f = self.road.update()
        self.D.append(d)
        self.F.append(f)

    def pause(self):
        """Met la simulation en pause."""
        


    def loop(self):
        return True



log.debug(f"{__name__} importé.")
