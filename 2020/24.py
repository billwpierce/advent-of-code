f = open('in24.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

# Part 1

flipped = []
for line in input:
    x, y, z = 0, 0, 0
    i = 0
    while i < len(line):
        if line[i] == "e":
            x, y, z = x+1, y-1, z
            i += 1
        elif line[i] == "w":
            x, y, z = x-1, y+1, z
            i += 1
        elif line[i] == "n":
            if line[i+1] == "e":
                x, y, z = x+1, y, z-1
                i += 2
            elif line[i+1] == "w":
                x, y, z = x, y+1, z-1
                i += 2
        elif line[i] == "s":
            if line[i+1] == "e":
                x, y, z = x, y-1, z+1
                i += 2
            elif line[i+1] == "w":
                x, y, z = x-1, y, z+1
                i += 2
    if (x, y, z) in flipped:
        flipped.remove((x, y, z))
    else:
        flipped.append((x, y, z))

print(len(flipped))

# Part 2

neighbors = [(1, -1, 0), (-1, 1, 0), (1, 0, -1), (-1, 0, 1), (0, 1, -1), (0, -1, 1)]

def count_neighbors(x, y, z, flipped):
    cnt = 0
    for n in neighbors:
        loc = (x+n[0], y+n[1], z+n[2])
        if loc in flipped:
            cnt += 1
    return cnt

for dn in range(100):
    accounted_for = []
    change = flipped.copy()
    for x, y, z in flipped:
        for dx, dy, dz in neighbors + [(0, 0, 0)]:
            loc = (x+dx, y+dy, z+dz)
            if loc in accounted_for:
                continue
            if loc in flipped: # Loc is black
                cn = count_neighbors(loc[0], loc[1], loc[2], flipped)
                if cn == 0 or cn > 2:
                    change.remove(loc)
            else:
                cn = count_neighbors(loc[0], loc[1], loc[2], flipped)
                if cn == 2:
                    change.append(loc)
            accounted_for.append(loc)
    flipped = change

print(len(flipped))

