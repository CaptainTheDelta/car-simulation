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
        

        if wait:
            for i in range(3,0,-1):
                log.info(i)
                sleep(1)


        log.info("Action !")



    def __del__(self):
        """Exécuté lorsque la simulation est finie."""
        pygame.quit()
        log.info("Coupez !")


    def update(self,n):
        self.screen.fill(bg)

        status = self.road.update()

        

        pygame.display.flip()
        sleep(n)


    def pause(self):
        """Met la simulation en pause."""
        


    def loop(self):
        for event in pygame.event.get():
            # quitter la simulation
            if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_q):
                return False
            # mettre la simulation en pause
            if event.type == pygame.KEYDOWN and event.key == K_p:
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_q):
                            return False
                        if (event.type == pygame.KEYDOWN and event.key == K_p):
                            return True
        return True



log.debug(f"{__name__} importé.")
