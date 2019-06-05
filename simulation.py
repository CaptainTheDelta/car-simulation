#!/usr/bin/env python3
# coding: utf-8

#------------------------------- argument parser ------------------------------

import argparse
import re

def fraction(string):
    if re.match(r"^(\d+\/\d+|\d+\.?\d*)$", string) != None:
        return eval(string)
    raise argparse.ArgumentTypeError(f"invalid value for fraction: '{string}'")


parser = argparse.ArgumentParser(description="Simulation d'une voie autoroutière.")

parser.add_argument("-l", "--road_length", help="longueur de la route", type=int, default=1800)
parser.add_argument("-p","--spawn_proba",  help="probabilité qu'un véhicule spawn", type=fraction, default=1/250)
parser.add_argument("-s","--max_speed",    help="limite de vitesse", type=int, default=50)

args = parser.parse_args()

#---------------------------------- includes ----------------------------------

import simulator

#--------------------------------- main loop ----------------------------------


for p in [1/50]:
    for i in range(1):
        road_sim = simulator.Simulator(
            road_length=args.road_length,
            spawn_proba=p,
            max_speed=args.max_speed
        )

while road_sim.loop():
    road_sim.update(0.003)