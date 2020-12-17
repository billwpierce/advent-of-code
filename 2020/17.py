f = open('in17.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

# input = [[input[y][x] for x in range(len(input[0]))] for y in range(len(input))]

class cubeState:
    active = "#"
    inactive = "."

# Part 1

known = {(-10, -10, 10)}

for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == cubeState.active:
            known.add((x, y, 0))

known.remove((-10, -10, 10))

def getCube(mp, x, y, z):
    if not (x, y, z) in mp:
        return cubeState.inactive
    return cubeState.active

neighbors = [(s, x, y) for s in range(-1, 2) for x in range(-1, 2) for y in range(-1, 2) if abs(s) + abs(x) + abs(y) != 0]

def getNearbyActive(mp, x, y, z):
    ret = 0
    for dx, dy, dz in neighbors:
        if getCube(mp, x+dx, y+dy, z+dz) == cubeState.active:
            ret += 1
    return ret

def updateSlices():
    toAdd = []
    toRemove = []
    for x, y, z in known:
        if getCube(known, x, y, z) == cubeState.active and not getNearbyActive(known, x, y, z) in range(2, 4):
            toRemove.append((x, y, z))
        for dx, dy, dz in neighbors:
            if getCube(known, x+dx, y+dy, z+dz) == cubeState.inactive and getNearbyActive(known, x+dx, y+dy, z+dz) == 3:
                toAdd.append((x+dx, y+dy, z+dz))
    for tpl in toAdd:
        if tpl in toRemove:
            raise Exception("what")
        else:
            known.add(tpl)
    for tpl in toRemove:
        known.remove(tpl)

for i in range(6):
    updateSlices()

print(len(known))

# Part 2

known = {(-10, -10, -10, -10)}

for y in range(len(input)):
    for x in range(len(input[0])):
        if input[y][x] == cubeState.active:
            known.add((x, y, 0, 0))

known.remove((-10, -10, -10, -10))

def getCube(mp, x, y, z, w):
    if not (x, y, z, w) in mp:
        return cubeState.inactive
    return cubeState.active

neighbors = [(s, x, y, w) for s in range(-1, 2) for x in range(-1, 2) for y in range(-1, 2) for w in range(-1, 2) if abs(s) + abs(x) + abs(y) + abs(w) != 0]

def getNearbyActive(mp, x, y, z, w):
    ret = 0
    for dx, dy, dz, dw in neighbors:
        if getCube(mp, x+dx, y+dy, z+dz, w + dw) == cubeState.active:
            ret += 1
    return ret

def updateSlices():
    toAdd = []
    toRemove = []
    for x, y, z, w in known:
        if getCube(known, x, y, z, w) == cubeState.active and not getNearbyActive(known, x, y, z, w) in range(2, 4):
            toRemove.append((x, y, z, w))
        for dx, dy, dz, dw in neighbors:
            if getCube(known, x+dx, y+dy, z+dz, w + dw) == cubeState.inactive and getNearbyActive(known, x+dx, y+dy, z+dz, w+dw) == 3:
                toAdd.append((x+dx, y+dy, z+dz, w+dw))
    for tpl in toAdd:
        if tpl in toRemove:
            raise Exception("what")
        else:
            known.add(tpl)
    for tpl in toRemove:
        known.remove(tpl)

for i in range(6):
    updateSlices()

print(len(known))
