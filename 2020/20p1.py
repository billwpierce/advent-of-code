f = open('in20t.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
# input = f.read().splitlines()  # Raw Reading
input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

input = [x.split("\n") for x in input]
# print(input)
tiles = {}
for i in input:
    tiles[int(i[0].split("Tile ")[1][:-1])] = i[1:]

def getTopBorder(index):
    return tiles[index][0]

def getBottomBorder(index):
    return tiles[index][-1]

def getLeftBorder(index):
    ret = ""
    tile = tiles[index]
    for i in range(10):
        ret += tile[i][0]
    return ret

def getRightBorder(index):
    ret = ""
    tile = tiles[index]
    for i in range(10):
        ret += tile[i][-1]
    return ret

def getAllBorders(index): # Borders go top, bottom, left, right
    return [getTopBorder(index), getBottomBorder(index), getLeftBorder(index), getRightBorder(index)]

borders = {}
all_borders = []

for key in tiles.keys():
    borders[key] = getAllBorders(key)
    all_borders.extend(getAllBorders(key))
    all_borders.extend([b[::-1] for b in getAllBorders(key)])

# print(borders)

def getMatchingBorders(index):
    my_borders = borders[index]
    out = [[] for i in range(4)]
    num_matching = [0, 0, 0, 0]
    for key in tiles.keys():
        for i in range(4):
            if key != index and (my_borders[i] in borders[key] or my_borders[i][::-1] in borders[key]):
                out[i].append(key)
                num_matching[i] += 1
    return out, num_matching

matching = {}
num_matching = {}

p = 1
corners = []
edges = []
for key in tiles.keys():
    matching[key], num_matching[key] = getMatchingBorders(key)
    if sum(num_matching[key]) == 2:
        p *= key
        corners.append(key)
    elif sum(num_matching[key]) == 3:
        edges.append(key)

# Part 1

print(p)

# dim = 12
dim = 3

orientations = [(False, 0), (False, 1), (False, 2), (False, 3), (True, 0), (True, 1), (True, 2), (True, 3)]
border_enum = {
    "top": 0,
    "bottom": 1,
    "left": 2,
    "right": 3
}
# Remember that to be flipped means to have each border flipped, not the tile flipped

def getKey(_dict, val):
    key_list = list(_dict.keys())
    val_list = list(_dict.values())
    return key_list[val_list.index(val)]

def getMutatedBorder(tile_key, border_number, orientation_number):
    if orientations[orientation_number][0]: # If flipped orientation
        return borders[tile_key][(border_number + orientations[orientation_number][1]) % 4][::-1]
    else:
        return borders[tile_key][(border_number + orientations[orientation_number][1]) % 4]


image = [[0 for i in range(dim)] for j in range(dim)]
rotations = [[() for i in range(dim)] for j in range(dim)]

pos = corners[0]
print(pos)
print(num_matching[pos])
nm = num_matching[pos]
dx, dy = 0, 0
if nm[0] == 1 and nm[2] == 1:
    x, y = dim-1, dim-1
    dx, dy = -1, 0
elif nm[0] == 1 and nm[3] == 1:
    x, y = 0, dim-1
    dx, dy = 0, 1
elif nm[1] == 1 and nm[2] == 1:
    x, y = dim-1, 0
    dx, dy = 0, -1
elif nm[1] == 1 and nm[3] == 1:
    x, y = 0, 0
    dx, dy = 1, 0
else:
    raise Exception("What")

image[y][x] = pos
rotations[y][x] = 0
rot = 0

cnrs = corners.copy()
cnrs.remove(pos)

edgs = edges.copy()

def pnti():
    print("Image:")
    print(image[0])
    print(image[1])
    print(image[2])

pnti()

neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def direction_to_border(direction):
    if direction == neighbors[0]:
        return border_enum["right"]
    elif direction == neighbors[1]:
        return border_enum["top"]
    elif direction == neighbors[2]:
        return border_enum["left"]
    elif direction == neighbors[3]:
        return border_enum["bottom"]
    else:
        raise Exception("ruh roh")

while True:
    x, y, = x+dx, y-dy
    print(x, y, dx, dy)
    if image[y][x] != 0:
        break
    options = []
    if x in [0, dim-1] and y in [0, dim-1]:
        options = cnrs
    else:
        options = edgs
    print(options, cnrs, edgs)
    for o in options:
        option_works = False
        print(o)
        for ori in range(len(orientations)):
            print([getMutatedBorder(pos,  direction_to_border((nx, ny)), rot) for nx, ny in neighbors], [getMutatedBorder(o,  direction_to_border((-nx, -ny)), ori) for nx, ny in neighbors])
            print([not(x+nx in range(0, dim and y+ny in range(0, dim)) and image[y+ny][x+nx] != 0) for nx, ny in neighbors], [getMutatedBorder(pos,  direction_to_border((nx, ny)), rot) == getMutatedBorder(o,  direction_to_border((-nx, -ny)), ori) for nx, ny in neighbors])
            if all([not(x+nx in range(0, dim and y+ny in range(0, dim)) and image[y+ny][x+nx] != 0) or getMutatedBorder(pos,  direction_to_border((nx, ny)), rot) == getMutatedBorder(o,  direction_to_border((-nx, -ny)), ori) for nx, ny in neighbors]):
                rot = ori
                option_works = True
                break
        if option_works:
            pos = o
            break
    print(options)
    if not pos in options:
        raise Exception("ruh roh")
    options.remove(pos)
    image[y][x] = pos
    rotations[y][x] = rot
    if dx == -1 and x == 0:
        dx, dy = 0, 1
    elif dx == 1 and x == dim - 1:
        dx, dy = 0, -1
    elif dy == -1 and y == dim-1:
        dx, dy = -1, 0
    elif dy == 1 and y == 0:
        dx, dy = 1, 0

pnti()