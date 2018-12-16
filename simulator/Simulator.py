# coding: utf-8
from .__init__ import *



class Simulator():
    """Simulateur."""

    def __init__(self,road_length,max_speed,spawn_proba,wait=False):
        """Initialise la simulation.

        Args:
            L (float): Longueur de la route.
            wait (bool): Démarage immédiat de la simulation, ou pas.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((road_length, 50))
        pygame.display.set_caption(f"Simulation d'une route")
        icon = pygame.image.load("simulator/img/car.png")
        pygame.display.set_icon(icon)


        self.road = Road("Voie 1",road_length,max_speed,spawn_proba)
        self.monitor = Monitor(self.road)
        

        if wait:
            sleep(1)
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
        trafficProblems = self.monitor.find_traffic_problems()

        for obj,x in status:
            obj.draw(self.screen,10)

        for tp in trafficProblems:
            tp.draw(self.screen,20)

        pygame.display.flip()

        sleep(n)


    def loop(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == pygame.KEYDOWN and event.key == K_q):
                return False
        return True