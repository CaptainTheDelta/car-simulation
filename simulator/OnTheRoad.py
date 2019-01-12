# coding: utf-8
from .__init__ import *



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
            color = [randint(0,255) for i in range(3)]
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




class Car(OnTheRoad):
    """Voiture. Vroom."""

    def __init__(self,v,a,length,width,color=[]):
        """Initialise une voiture.

        Args:
            v (float): Vitesse de la voiture (m.s-1).
            a (float): Accélération (m.s-2).
            length (float): Longueur de la voiture.
            width (float): Largeur de la voiture.
            color (list): Couleur (rgb) de la voiture.
        """
        super().__init__(0,length,width,color)

        self.v = v
        self.vMax = v
        self.a = a

        self.reactionTime = 0

        log.info(self.colored(f"Voiture n°{self.id} créée. v={v}, a={a}"))

    def get_speed(self):
        """Renvoie la vitesse de la voiture.

        Return:
            (float): Renvoie la vitesse de la voiture.
        """
        return self.v

    def security(self):
        """Renvoie la distance de sécurité que la voiture de derrière doit
        respecter.

        Returns:
            (float): Distnce de sécurité.
        """
        return self.v * 6 // 10 + 2

    def move(self,obj=None):
        """Fait avancer la voiture, en fonction de la présence d'un objet 
        devant elle.

        Args:
            d (float): Distance.
        """
        if self.v == 0 and 0 < self.reactionTime < 2:
            # if obj != None:
            #     if obj.get_pos() - self.pos - obj.get_length() > 1.1*SAFETY_DISTANCE:
            #         log.debug(self.colored("Rebond ?"))
            self.reactionTime += DT
            return self.pos

        elif self.reactionTime >= 2:
            self.reactionTime = 0

        v = min(self.v + self.a * DT, self.vMax)

        if obj != None:
            dist = obj.get_pos() - self.pos - obj.get_length()
            sec = max(0,dist - obj.security())
            v = min(v, sec/DT)
            
            if self.v != 0 and v == 0 and obj.get_speed() > 0:
                log.debug(self.colored("Rebond ?"))

        if v == 0:
            log.debug(self.colored(f"{self.id} Arrêt soudain !"))
            self.reactionTime += DT

        self.v = v
        self.pos += v * DT

        if self.v - self.vMax > 1e-12:
            log.warning(self.colored(f"Flash ! {self.id} à {self.v} > {self.vMax}"))
        if v < 0:
            log.warning(self.colored(f"{self.id} Vitesse négative !"))

        return self.pos


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