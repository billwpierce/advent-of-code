f = open('d9.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

input = [[int(x) for x in line] for line in input]
height = len(input)
width = len(input[0])
adjacencies = [(-1, 0), (0, -1), (1, 0), (0, 1)]

## Part 1

basins_ends = []

risk = 0

for y in range(len(input)):
    line = input[y]
    for x in range(len(line)):
        val = line[x]
        bottom = True
        for adj in adjacencies:
            new_pos = (y + adj[0], x + adj[1])
            if (new_pos[0] < 0 or new_pos[0] > height - 1 or new_pos[1] < 0 or new_pos[1] > width - 1):
                pass
            else:
                pos = input[y + adj[0]][x + adj[1]]
                if pos <= val:
                    bottom = False
        if bottom:
            print(val)
            risk += val + 1
            basins_ends.append((y, x))

print(risk)

## Part 2

basin_sizes = [0 for i in basins_ends]

def simulate_flow(y, x):
    val = input[y][x]
    if val == 9:
        return
    descended = True
    # print(y, x, adjacencies)
    min_desc = 10
    while descended:
        descended = False
        y_prime, x_prime = y, x
        for adj in adjacencies:
            new_pos = (y + adj[0], x + adj[1])
            # print(new_pos)
            if (new_pos[0] < 0 or new_pos[0] > height - 1 or new_pos[1] < 0 or new_pos[1] > width - 1):
                pass
            else:
                pos = input[y + adj[0]][x + adj[1]]
                # print(new_pos, pos)
                if pos < min_desc:
                    min_desc = pos
                    y_prime, x_prime = new_pos[0], new_pos[1]
                    descended = True
        val = input[y][x]
        y, x = y_prime, x_prime
        # print(val)
    # print(y, x)
    # print(basin_sizes, basins_ends)
    basin_sizes[basins_ends.index((y, x))] += 1

for y in range(len(input)):
    line = input[y]
    for x in range(len(line)):
        val = line[x]
        # print(y, x)
        simulate_flow(y, x)

def mult_list(lst):
    mul = 1
    for el in lst:
        mul *= el
    return mul

print(mult_list(sorted(basin_sizes, reverse=True)[:3]))
