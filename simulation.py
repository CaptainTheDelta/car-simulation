#!/usr/bin/env python3
# coding: utf-8

#---------------------------------- includes ----------------------------------

import simulator
import csv

#--------------------------------- main loop ----------------------------------

L = 2000
speed = 36
speeds = [8.3, 13.9, 25, 30.5, 36]

with open("res.csv", 'w') as csvfile:
    reswriter = csv.writer(csvfile)
    
    for speed in speeds:
        for p in range(10):
            p = (p+1) / 10

            for i in range(3):
                road_sim = simulator.Simulator(
                    road_length=L,
                    spawn_proba=p,
                    max_speed=speed
                )

                n = 0
                while n < 50000:
                    road_sim.update(0.003)
                    n += 1

                d,f = road_sim.get_res()

                print(f"route p:{p} v:{speed} terminée -> {d}, {f}")
                reswriter.writerow([speed, p, d, f])