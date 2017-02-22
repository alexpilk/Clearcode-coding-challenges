# Script for generating random terrains.
# To generate a terrain run the script and specify the dimensions.
# For example: python terrain_generator.py 17

import random
import sys

dimensions = int(sys.argv[1])
terrain = []

output = open('generated_terrain.txt','w')
output.write(str(dimensions)+"\n")
for i in range(dimensions):
    for j in range(dimensions):
        output.write(str(random.randint(1,9)))
        if j!=dimensions-1:
            output.write(",")
    if i!=dimensions-1:
        output.write("\n")
