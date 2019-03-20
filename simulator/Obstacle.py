# coding: utf-8
from simulator.__init__ import *



class Obstacle(OnTheRoad):
    """Obstacle."""

    def __init__(self,pos,length,width,ti,tf,color=-1):
        """Initialise un obstacle.

        Args:
            pos (float): Position de l'obstacle.
            ti (float): Instant d'apparition de l'obstacle.
            tf (float): Instant de disparition de l'obstacle.
            color (int): Couleur de la voiture.
        """
        super().__init__(pos,length,width,color)

        self.ti = ti
        self.tf = tf


    def get_ti(self):
        """Renvoie l'instant d'apparition de l'obstacle.

        Return:
            (float): Temps.
        """
        return self.ti

    def get_ti(self):
        """Renvoie l'instant de disparition de l'obstacle.

        Return:
            (float): Temps.
        """
        return self.tf


log.debug(f"{__name__} importé.")