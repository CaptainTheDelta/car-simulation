#!/usr/bin/env python3
# coding: utf-8

#---------------------------------- includes ----------------------------------

import simulator

#--------------------------------- main loop ----------------------------------

L = 2000
speed = 36

for p in [1/50]:
    for i in range(1):
        road_sim = simulator.Simulator(
            road_length=L,
            spawn_proba=p,
            max_speed=speed
        )

        n = 0
        while n < 2000:
            road_sim.update(0.003)
            n += 1