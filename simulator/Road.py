# coding: utf-8
from simulator.__init__ import *



class Road():
    """Route."""

    def __init__(self,name,L,vMax,p,obs=[]):
        """Initialise une route.
        vMax est la limitation de vitesse de la route, il est possible que les
        voitures aillent plus vite...

        Args:
            name (str): Nom de la route.
            L (float): Longueur de la route.
            vMax (float): Vitesse maximale (m.s-1).
            p (float): Probabilité qu'une voiture arrive sur la route à chaque instant.
            obs (list): Liste d'objet Obstacle.
        """
        self.name = name
        
        self.L = L
        self.vMax = vMax
        self.p = p

        self.cars = []
        self.status = {}

        self.obsToSpawn = obs
        self.obsSpawned = []
        
        self.t = 0

    def __repr__(self):
        """Renvoie une description de la route."""
        n = len(self.cars)
        o = 0
        return f"{self.name} : {n} voiture{s(n)}, {o} obstacle{s(0)}"

    def get_length(self):
        """Renvoie la longueur de la route.

        Return:
            (float): longueur de la route.
        """
        return self.L 


    def spawn_car(self):
        """Ajoute une voiture sur la route."""
        a = ACCELERATION
        v = gauss(self.vMax,5)

        if v < 0:
            log.warning("Véhicule à vitesse négative.")
            return
        
        car = Car(v,a,randint(2,5),2)
        self.status[car] = 0
        self.cars.append(car)


    def get_current_status(self):
        """Renvoie une liste contenant [obj,pos] de chacun de l'ensemble des
        objets sur la route.

        Return:
            (list): Description de la route.
        """
        return sorted(self.status.items(),key=itemgetter(1))


    def move_car(self,car,obj=None):
        """Fait avancer la voiture d'une certaine distance.
        Si la voiture sort de la route, elle est désintégrée.

        Args:
            car (Car): Voiture.
            d (float): Distance.
        """
        p = car.get_pos()
        pos = car.move(obj)
        
        if obj != None:
            if pos > obj.get_pos():
                log.warning(car.colored("DÉPASSEMENT PAR LE MILIEU"))
        
        if pos < self.L:
            self.status[car] = pos
        else:
            car.debug(f"suppression : {pos} > {self.L}")
            self.cars.remove(car)
            del self.status[car]


    def update(self):
        """Update la route au temps."""
        # log.info(f"{self.t:.3f}".center(20,"-"))
        self.t += DT

        # on récupère la liste des objets sur la route :
        objects = sorted(self.status.items(),key=itemgetter(1))
        n = len(objects)
        
        # on update les voitures
        for i,(obj,pos) in enumerate(objects):
            if type(obj) == Car:
                if i < n - 1:
                	self.move_car(obj,objects[i+1][0])
                else:
                    self.move_car(obj)

        # On tente de faire spawn une voiture
        if len([o for o,x in self.status.items() if x < o.security()]) == 0:
            if random() <= self.p:
                self.spawn_car()

        return sorted(self.status.items(),key=itemgetter(1))


log.debug(f"{__name__} importé.")