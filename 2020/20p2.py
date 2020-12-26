f = open('in20.txt', 'r') # Insert the correct day
input = f.read().split("\n\n") # Groups Across Multiple Lines

input = [x.split("\n") for x in input]
# print(input)
tiles = {}
for i in input:
    tiles[int(i[0].split("Tile ")[1][:-1])] = i[1:]

def getTopBorder(tile):
    return tile[0]

def getBottomBorder(tile):
    return tile[-1]

def getLeftBorder(tile):
    ret = ""
    for i in range(10):
        ret += tile[i][0]
    return ret

def getRightBorder(tile):
    ret = ""
    for i in range(10):
        ret += tile[i][-1]
    return ret

def print_tile(tile):
    for line in tile:
        print(line)

def flip_tile(tile):
    new_tile = []
    for i in range(len(tile)):
        new_tile.append(tile[i][::-1])
    return new_tile

def rotate_tile(tile, num_rotations, size=10):
    cp = tile.copy()
    for i in range(num_rotations):
        temp = []
        for j in range(size):
            new_line = ""
            for k in range(size):
                new_line += cp[size-k-1][j]
            temp.append(new_line)
        cp = temp
    return cp

all_borders = {}
for key in tiles.keys():
    all_borders[key] = [getTopBorder(tiles[key]), getRightBorder(tiles[key]), getBottomBorder(tiles[key]), getLeftBorder(tiles[key]), getTopBorder(flip_tile(tiles[key])), getRightBorder(flip_tile(tiles[key])), getBottomBorder(flip_tile(tiles[key])), getLeftBorder(flip_tile(tiles[key]))]

image = {}
image_keys = {}

image[(0, 0)] = tiles[list(tiles.keys())[0]]
image_keys[(0, 0)] = list(tiles.keys())[0]

neighbors = [(0, -1), (1, 0), (0, 1), (-1, 0)]

available_keys = list(tiles.keys())

def print_image(image_dict):
    earliest_x, latest_x = min([x[0] for x in list(image_dict.keys())]), max([x[0] for x in list(image_dict.keys())])
    earliest_y, latest_y = min([x[1] for x in list(image_dict.keys())]), max([x[1] for x in list(image_dict.keys())])
    for y in range(earliest_y, latest_y+1):
        for r in range(10):
            for x in range(earliest_x, latest_x + 1):
                if not (x, y) in list(image_dict.keys()):
                    print(" "*11, end="")
                    continue
                print(image_dict[(x, y)][r], end=" ")
            print("\n", end="")
        print("\n", end="")

def recurse(x, y):
    for i in range(4):
        dx, dy = neighbors[i]
        nx, ny = x+dx, y+dy
        if (nx, ny) in image:
            continue        
        if i == 0:
            btm = getTopBorder(image[(x, y)])
        elif i == 1:
            btm = getRightBorder(image[(x, y)])
        elif i == 2:
            btm = getBottomBorder(image[(x, y)])
        elif i == 3:
            btm = getLeftBorder(image[(x, y)])
        success = False
        for key in tiles.keys():
            if key == 3079 and (nx, ny) == (1, 0):
                print("okay")
            if success:
                break
            if key != image_keys[(x, y)]: # and btm in all_borders[key]
                for f in [True, False]:
                    if success:
                        break
                    for rot in range(4):
                        if success:
                            break
                        new_tile = tiles[key]
                        if f:
                            new_tile = flip_tile(new_tile)
                        new_tile = rotate_tile(new_tile, rot)
                        if i == 0 and getBottomBorder(new_tile) == btm:
                            image[(nx, ny)] = new_tile
                            image_keys[(nx, ny)] = key
                            success = True
                            recurse(nx, ny)
                        elif i == 1 and getLeftBorder(new_tile) == btm:
                            image[(nx, ny)] = new_tile
                            image_keys[(nx, ny)] = key
                            success = True
                            recurse(nx, ny)
                        elif i == 2 and getTopBorder(new_tile) == btm:
                            image[(nx, ny)] = new_tile
                            image_keys[(nx, ny)] = key
                            success = True
                            recurse(nx, ny)
                        elif i == 3 and getRightBorder(new_tile) == btm:
                            image[(nx, ny)] = new_tile
                            image_keys[(nx, ny)] = key
                            success = True
                            recurse(nx, ny)

recurse(0, 0)

print("Unassembled image:")
print_image(image)
print(list(image.keys()))

def assemble_image(image_dict):
    earliest_x, latest_x = min([x[0] for x in list(image_dict.keys())]), max([x[0] for x in list(image_dict.keys())])
    earliest_y, latest_y = min([x[1] for x in list(image_dict.keys())]), max([x[1] for x in list(image_dict.keys())])
    out = []
    for y in range(earliest_y, latest_y+1):
        for r in range(1, 9):
            new_line = ""
            for x in range(earliest_x, latest_x+1):
                new_line += image_dict[(x, y)][r][1:9]
            out.append(new_line)
    return out

print("Assembled image:")
asm = assemble_image(image)
print_tile(asm)
print(len(asm))
print(len(asm[0]))

def getSeaMonsters(ai):
    cnt = 0
    for y in range(len(ai) - 3):
        for x in range(len(ai[0]) - 20):
            if ai[0] == ".#.#..#.##...#.##..#####" and x == 2 and y == 3:
                pass
            if ai[y][x+18] == "#":
                if ai[y+1][x+0] == "#" and ai[y+1][x+5] == "#" and ai[y+1][x+6] == "#" and ai[y+1][x+11] == "#" and ai[y+1][x+12] == "#" and ai[y+1][x+17] == "#" and ai[y+1][x+18] == "#" and ai[y+1][x+19] == "#":
                    if ai[y+2][x+1] == "#" and ai[y+2][x+4] == "#" and ai[y+2][x+7] == "#" and ai[y+2][x+10] == "#" and ai[y+2][x+13] == "#" and ai[y+2][x+16] == "#":
                        cnt += 15
    return cnt

cnt = 0

for f in [True, False]:
    for rot in range(4):
        t = asm.copy()
        if f:
            t = flip_tile(t)
        t = rotate_tile(t, rot, len(t))
        if getSeaMonsters(t) > 0:
            cnt = getSeaMonsters(t)
            print(cnt)

total = sum([line.count("#") for line in asm])

out = total - cnt
print(out)