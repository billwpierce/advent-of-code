f = open('d2.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

distance, depth = 0, 0
aim = 0
for direction, number in input:
    num = int(number)
    if direction == "forward":
        distance += num
        depth += num * aim
    elif direction == "up":
        aim -= num
    else:
        aim += num

print(depth * distance)