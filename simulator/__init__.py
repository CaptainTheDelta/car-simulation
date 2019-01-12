# coding: utf-8
import pygame
from pygame.locals import *
from random import randint, gauss, random
from operator import itemgetter
from time import sleep
import logging as log
import sty

#----------------------------- réglages des logs ------------------------------
log.basicConfig(format='[%(levelname)s] %(message)s',level=log.DEBUG)
# log.disable()

from .config import *
from .fonctions import *
from .OnTheRoad import *
from .Road import *
from .Monitor import *
from .Simulator import *