f = open('in12.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # @d array of the input

import math

# print(input)

# Part 1

locx = 0
locy = 0
dirc = 0

for line in input:
    action = line[0]
    num = int(line[1:])
    if action == "F":
        locx += math.cos(math.radians(dirc)) * num
        locy += math.sin(math.radians(dirc)) * num
    elif action == "N":
        locy += num
    elif action == "S":
        locy -= num
    elif action == "W":
        locx -= num
    elif action == "E":
        locx += num
    elif action == "L":
        dirc += num
    elif action == "R":
        dirc -= num
    else:
        raise Exception("what")

print(abs(locx) + abs(locy))

# Part 2

locx = 0
locy = 0

wayx = 10
wayy = 1

for line in input:
    action = line[0]
    num = int(line[1:])
    if action == "F":
        locx += num * wayx
        locy += num * wayy
    elif action == "N":
        wayy += num
    elif action == "S":
        wayy -= num
    elif action == "W":
        wayx -= num
    elif action == "E":
        wayx += num
    else:
        rot = num
        if action == "R":
            rot = 360 - num
        if rot == 90:
            wayx, wayy = -wayy, wayx
        elif rot == 180:
            wayx, wayy = -wayx, -wayy
        elif rot == 270:
            wayx, wayy = wayy, -wayx

print(abs(locx) + abs(locy))
