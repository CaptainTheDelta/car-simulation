# coding: utf-8

import simulator as sim
from simulator.config import *

#--------------------------------- main loop ----------------------------------

simulator = sim.Simulator(
    road_length=ROAD_LENGTH,
    spawn_proba=1/50,
    max_speed=50
)

while simulator.loop():
    simulator.update(0.003)