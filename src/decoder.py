

class Decoder:
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
    import sys 


    def convolve_hamming(data: list) -> tuple:
        # Lo saltamos si es muy corto i.e. < min(len(stations)) o si es muy largo 100 (arbitrario, pero mayor que la estación más
        # larga)
        if len(data) < 26 or len(data) > 100 : return None, None

        min_dist = 10000
        station = None
        for callsign, bits in stations.items():
            # y es el vector que movemos sobre x, entonces 'y' tiene que ser el de menor tamaño
            if len(data) > len(bits):
                x = data
                y = bits
            else:
                x = bits
                y = data
            max_i = len(x) - len(y)

            for i in range(max_i):
                # El error es la distancia hamming del vector a la estación más lo que sobra/no llega
                hamming_dist = sum(map(lambda x: x[0] ^ x[1], zip(y,x[i:i+len(y)]))) + max_i 
                if hamming_dist < min_dist: min_dist = hamming_dist; station = callsign

        return (station, min_dist)

