""" 
==============
Decoder System
==============

Takes as input an array of bits and returns the station that best matches the array. The criterion used is the minimun Hamming
distance between the stations and the shifted input array (like a running hamming distance of the array with every station)

"""

import sys 
from multiprocessing import Pipe


stations = {'4U1UN':  [1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,
                       0,0,0,1,1,1,0,1,0],
            'VE8AT':  [1,0,1,0,1,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,0,0,1,1,1,0],
            'W6WX':   [1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0],
            'KH6RS':  [1,1,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,
                       1,0,1,0],
            'ZL6B':   [1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0],
            'VK6RBP': [1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,
                       0,1,0,1,0,1,0,0,0,1,0,1,1,1,0,1,1,1,0,1,0],
            'JA2IGY': [1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0,1,1,1,
                       0,1,1,1,0,1,0,0,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0],
            'RR9O':   [1,0,1,1,1,0,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,0,0,1,1,1,0,1,1,1,0,
                       1,1,1,0],
            'VR2B':   [1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0],
            '4S7B':   [1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0],
            'ZS6DN':  [1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,0,0,1,1,
                       1,0,1,0],
            '5Z4B':   [1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0],
            '4X6TU':  [1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,0,0,
                       1,0,1,0,1,1,1,0],
            'OH2B':   [1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,
                       1,0,1,0,1,0],
            'CS3B':   [1,1,1,0,1,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0],
            'LU4AA':  [1,0,1,1,1,0,1,0,1,0,0,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,1,1,0],
            'OA4B':   [1,1,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,1,1,0,1,0,1,0,1,0],
            'YV5B':   [1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0]
            }


class Decoder:

    def __init__(self):
        # Aquí no hace falta guardar estado, ya que cada llamada es totaltmente independiente de la anterior, no hay memoria
        pass 

    def decoder(self, pipe_in, pipe_out) -> None:
        while True:
            data = pipe_in.recv()
            # Lo saltamos si es muy corto i.e. < min(len(stations)) o si es muy largo 100 (arbitrario, pero mayor que la estación más
            # larga)
            if len(data) < 26 or len(data) > 100: pipe_out.send(())
            else:
                min_dist = 10000
                station = None
                for callsign, bits in stations.items():
                    # 'y' es el vector que movemos sobre x, entonces 'y' tiene que ser el de menor tamaño
                    if len(data) > len(bits):
                        x = data
                        y = bits
                    else:
                        x = bits
                        y = data
                    max_i = len(x) - len(y)

                    for i in range(max_i):
                        # El error es la distancia hamming del vector que recibimos al vector de la estación más el número de
                        # elementos que sobran/faltan entre ellos
                            # TODO: es esto lo mejor?
                        hamming_dist = sum(map(lambda x: x[0] ^ x[1], zip(y,x[i:i+len(y)]))) + max_i 
                        if hamming_dist < min_dist: min_dist = hamming_dist; station = callsign
                # Enviamos lo que tenemos por la pipe al proceso principal
                pipe_out.send((station, min_dist))
