# coding: utf-8
from simulator.__init__ import *


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
        

log.debug(f"{__name__} importé.")