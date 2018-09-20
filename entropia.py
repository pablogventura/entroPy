import math
import sys

cantidades = {}
for i in range(256):
    cantidades[i] = 0.0

total = 0.0

while True:
    try:
        bytes = raw_input()
    except EOFError:
        for i in range(256):
            cantidades[i] = float(cantidades[i]) / float(total)
            if cantidades[i]:
                cantidades[i] = (-1) * cantidades[i] * math.log(cantidades[i], 256)

        print sum(cantidades.values())
        sys.exit(0)
    total += len(bytes)
    for byte in range(256):
        cantidades[byte] += bytes.count(chr(byte))


