f = open('d5.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

size = 1000
grid = [[0 for i in range(size)] for j in range(size)]

for line in input:
    vent = [[int(x) for x in l.split(',')] for l in line.split(" -> ")]
    if vent[0][0] == vent[1][0]: # Vertical
        x = vent[0][0]
        for i in range(min(vent[0][1], vent[1][1]), max(vent[0][1], vent[1][1])+1):
            grid[i][x] += 1
    elif vent[0][1] == vent[1][1]: # Horizontal
        y = vent[0][1]
        for j in range(min(vent[0][0], vent[1][0]), max(vent[0][0], vent[1][0])+1):
            grid[y][j] += 1
    else: # diagonal
        x_change = vent[1][0] - vent[0][0]
        x_mag = 1 if x_change > 0 else -1
        y_change = vent[1][1] - vent[0][1]
        y_mag = 1 if y_change > 0 else -1
        mag_change = abs(x_change)
        for i in range(mag_change + 1):
            x = vent[0][0] + i*x_mag
            y = vent[0][1] + i*y_mag
            grid[y][x] += 1

ret = sum([sum([1 for j in range(size) if grid[j][i] >= 2]) for i in range(size)])
print(ret)
    