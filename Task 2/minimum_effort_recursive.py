# This script solves Task 2 recursively.
# It's not a perfect solution either,
# since it takes 7.4 seconds on my machine to check a 17x17 terrain.
# But it's still much faster than the previous solution using itertools.
# Run this script from terminal/cmd by typing
# python minimum_effort_recursive.py "file_with_terrain.txt"

import sys

f = open(sys.argv[1],'r').read()
f = f.split('\n')

# Spliting the input file into a list of nxn terrains.
terrains = []
row_index = 0
while row_index < len(f):
	dimensions = int(f[row_index])
	current_terrain = f[row_index+1 : row_index+1+dimensions]
	for i in range(len(current_terrain)):
		current_terrain[i] = current_terrain[i].split(',')
		for el in range(len(current_terrain[i])):
					current_terrain[i][el] = int(current_terrain[i][el])
	terrains.append(current_terrain)
	row_index += dimensions + 1

# Sets min_energy to the maximum possible energy
# before checking the terrain.
min_energy = len(terrains[0])*2*9

def walker(terrain, position, en):
	"""
	Recursively checks every possible route.
	Args:
		terrain: two-dimantional list of energies in the terrain.
		position: start position for "walking".
		en: the energy the current rout has taken so far.
	Returns:
		nothing.
	"""

	global min_energy

	# Checks if current energy consumption exceeded minimum energy.
	if en>=min_energy:
		return

	# Checks if it is the last cell in a row.
	# If yes - continues to check only the last column.
	if position[0] == len(terrain)-1:
		while position[1] < len(terrain)-1:
			position[1]+=1
			en += terrain[position[0]][position[1]]
			if en>min_energy:
				return
		min_energy = en
		return

	# Checks if it is the last cell in a column.
	# If yes - continues to check only the last row.
	if position[1] == len(terrain)-1:
		while position[0] < len(terrain)-1:
			position[0]+=1
			en += terrain[position[0]][position[1]]
			if en>min_energy:
				return
		min_energy = en
		return

	# The code above can be rewritten the following way:
	#
	# for p in range(2):
	# 	if position[p] == len(terrain)-1:
	# 		while position[p-1] < len(terrain)-1:
	# 			position[p-1]+=1
	# 			en += terrain[position[0]][position[1]]
	# 			if en>energies[-1]:
	# 				return
	# 		energies.append(en)
	# 		return
	#
	# But it's faster and more readable without the loop.

	# Starts walker function from the adjacent cells.
	walker(terrain, [position[0],position[1]+1], en + terrain[position[0]][position[1]+1])
	walker(terrain, [position[0]+1,position[1]], en + terrain[position[0]+1][position[1]])

# Loop for checking all the terrains.
for t in terrains:
	walker(t, [0,0], t[0][0])
	print(min_energy)
	min_energy = len(t)*2*9
