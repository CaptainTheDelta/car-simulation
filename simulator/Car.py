# coding: utf-8
from simulator.__init__ import *



class Car(OnTheRoad):
    """Voiture. Vroom."""

    def __init__(self,v,a,color=[]):
        """Initialise une voiture.

        Args:
            v (float): Vitesse de la voiture (m.s-1).
            a (float): Accélération (m.s-2).
            color (list): Couleur (rgb) de la voiture.
        """
        super().__init__(0,1,2,color)

        self.v = v
        self.vMax = v
        self.acc = 3
        self.dcc = -2

        self.reactionTime = 0

        # self.info(f"Voiture n°{self.id} créée. v={v}, a={a}")

    def __del__(self):
        """Supprime la voiture."""
        # self.info(f"Voiture n°{self.id} sortie.")

    def __repr__(self):
        return self.colored(f"Car n°{self.id}")

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
        if self.v == 0:
            if obj != None:
                vf = obj.get_speed()
                sec = self.security()
                Δx = obj.get_pos() - self.pos

                if vf == 0 and Δx <= sec:
                    return self.pos

            if 0 <= self.reactionTime < 2:
                self.reactionTime += DT
                return self.pos
            else:
                self.reactionTime = 0

        v = min(self.v + self.acc * DT, self.vMax)

        if obj != None:
            vf = obj.get_speed()
            sec = obj.security()
            Δx = obj.get_pos() - self.pos

            if (v-vf) * DT > Δx-sec:
                T = (vf - self.v) / self.dcc
                d = 1/2 * self.dcc * T ** 2 + self.v * T

                dist = (vf * T + Δx) - d

                if sec < dist < 1.1*sec:
                    v = max(0, self.v + self.dcc * DT)

                T = (vf - v) / self.dcc
                d = 1/2 * self.dcc * T ** 2 + v * T
                dist = (vf * T + Δx) - d                

                if (v-vf) * DT > Δx-sec:
                    dcc =  - (vf - self.v) ** 2 / (2*(Δx-sec))
                    # vp = v
                    v = max(0, self.v + dcc * DT)

                if (v-vf) * DT > Δx-sec:
                    v = 0.9*vf

        self.v = v
        self.pos += v * DT

        return self.pos


log.debug(f"{__name__} importé.")