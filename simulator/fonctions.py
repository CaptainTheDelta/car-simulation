# coding: utf-8

s = lambda n: 's' if n else ''

def ms2kmh(v):
    """Convertie une vitesse m/s en km/h.

    Args:
        v (float): Vitesse en m/s.

    Return:
        (float): Vitesse en km/h.
    """
    return v * 3.6


def kmh2ms(v):
    """Convertit une vitesse km/h en m/s.

    Args:
        v (float): Vitesse en km/h.

    Return:
        (float): Vitesse en m/s.
    """
    return v / 3.6


from simulator.__init__ import *