# coding: utf-8
from simulator.__init__ import *



class OnTheRoad():
    """Classe mère des objets sur la route."""
    _id = 0
    
    def __init__(self,pos,length,width,color=[]):
        """Initialise un  objet sur la route.

        Args:
            pos (float): Position de l'objet sur la route.
            length (float): Longueur de l'objet.
            width (float): Largeur de l'objet.
            color (list): Couleur de l'objet (rgb).
        """
        self.pos = pos
        self.l = length
        self.w = width

        if color == []:
            treshold = 255
            r = randint(0,255)
            g = randint(int(sqrt(max(0,(treshold**2-r**2)/2))),255)
            b = randint(int(sqrt(max(0,treshold**2-r**2-g**2))),255) 
            color = [r,g,b]
            shuffle(color)
        self.color = color
        
        self.id = type(self)._id
        type(self)._id += 1


    def get_pos(self):
        """Renvoie la position de l'objet sur la route.

        Return:
            (float): Position.
        """
        return self.pos

    def get_id(self):
        """Renvoie l'id de l'objet.
        L'id est compté par classe.

        Return:
            (int): Id de l'objet.
        """
        return self.id

    def get_total_spawned(self):
        """Renvoie le nombre d'objet d'une classe créés.
        Renvoie la valeur du compteur de la classe.

        Return:
            (int): Nombre.
        """
        return type(self)._id

    def get_color(self):
        """Renvoie la couleur de l'objet.

        Return:
            (tuple): RGB.
        """
        return self.color

    def get_length(self):
        """Renvoie la longueur de l'objet.

        Return:
            (float): Longueur.
        """
        return self.l

    def colored(self,txt):
        """Renvoie le texte écrit avec la couleur de l'objet.

        Args:
            txt (str): Texte.

        Returns:
            (str): Texte coloré.
        """
        return sty.fg(*self.color) + str(txt) + sty.fg.rs

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

    def debug(self,txt):
        """Debug du texte avec la couleur de l'objet.

        Args:
            txt (str): texte.
        """
        log.debug(self.colored(txt))

    def warning(self,txt):
        """Alerte avec le texte avec la couleur de l'objet.

        Args:
            txt (str): texte.
        """
        log.warning(self.colored(txt))

    def info(self,txt):
        """Informe avec le texte avec la couleur de l'objet.

        Args:
            txt (str): texte.
        """
        log.info(self.colored(txt))


log.debug(f"{__name__} importé.")