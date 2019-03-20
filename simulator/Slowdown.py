# coding: utf-8
from simulator.__init__ import *


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