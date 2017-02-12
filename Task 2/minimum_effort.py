import itertools

f = open("terrains.txt",'r').read()
print("Input terrains: \n{0}".format(f))
f = f.split('\n')

# spliting the input file into a list of nxn terrains
terrains = []
row_index = 0
while row_index < len(f):
    dimensions = int(f[row_index])
    current_terrain = f[row_index+1 : row_index+1+dimensions]
    for i in range(len(current_terrain)):
        current_terrain[i] = current_terrain[i].split(',')
    terrains.append(current_terrain)
    row_index += dimensions + 1


# function for finding all possible routes
def router(terrain):
    number_of_steps = (len(terrain)-1) * 2
    possible_routes = []
    # perm_string consists of characters R (move right) and D (move down)
    # number of Rs must = number of Ds
    perm_string = ''
    for i in range(int(number_of_steps / 2)):
        perm_string += 'RD'
    # finding all possible permutations
    for p in itertools.permutations(perm_string): 
        possible_routes.append(p)
    # removing duplicates
    return set(possible_routes)


# function for testing every possible route
def walk(terrain):
    all_routes = router(terrain)
    min_energy = -1 
    for route in router(terrain):
        # energy in position [0,0]
        energy = int(terrain[0][0])
        position = [0,0]
        for move in route:
            if move == 'D': 
                position[0] += 1
            elif move == 'R':
                position[1] += 1
            energy += int(terrain[position[0]][position[1]])
        if energy < min_energy or min_energy == -1:
            min_energy = energy
    return min_energy


output = open('min_energy.txt','w')
for t in terrains:
    min_energy = str(walk(t))
    print("Min energy: {0}".format(min_energy))
    output.write(min_energy + "\n")
