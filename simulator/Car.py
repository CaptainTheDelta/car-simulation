# coding: utf-8
from simulator.__init__ import *



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
        self.acc = a
        self.dcc = -20

        self.reactionTime = 0

        self.info(f"Voiture n°{self.id} créée. v={v}, a={a}")

    def __del__(self):
        """Supprime la voiture."""
        self.info(f"Voiture n°{self.id} sortie.")

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
            self.reactionTime += DT
            return self.pos

        elif self.reactionTime >= 2:
            self.reactionTime = 0

        v = min(self.v + self.acc * DT, self.vMax)

        if obj != None:
            v_obj = obj.get_speed()

            if v_obj < self.v:
                dist = obj.get_pos() - self.pos - self.get_length()
                sec = obj.security()



                # calcul de la distance séparant les deux véhicules si le
                # deuxième commençait à déccelerer maintenant :
                d = dist + (v_obj - self.v)**2 / (2*self.dcc)
                T = (v_obj - self.v) / self.dcc


                # if self.id == 1:
                #     self.debug(f"ralentissement safe: {d:.3f} - {dist:.3f} ({sec}) => {self.v} {v_obj}")


                if d < sec:

                    # LÀ IL FAUT RECALCULER L'ACCÉLÉRATION NÉCESSAIRE !!!
                    dcc = - 2 * (dist + (self.v-v_obj)*T)/T**2
                    v = max(0, self.v + dcc * DT)
                    if dcc > 0:
                        self.warning(f"FUSÉE ! dcc : {dcc}")

                    if self.id == 1:
                        self.debug(f"Ralentissement : {abs(self.v-v)}")

                    # self.debug(f"On ralentit {self.v} -> {v}")
                # else:
                #     self.debug(f"On accélère {self.v} -> {v}")

        self.v = v
        self.pos += v * DT


        # if v == 0:
        #     self.reactionTime += DT
        #     self.debug(f"{self.id} Arrêt soudain !")
        

        # if self.v - self.vMax > 1e-12:
            # self.warning(f"Flash ! {self.id} à {self.v} > {self.vMax}")
        # if v < 0:
        #     self.warning(f"{self.id} Vitesse négative !")

        return self.pos


log.debug(f"{__name__} importé.")