f = open('d7.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
# input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

input = [int(x) for x in f.read().splitlines()[0].split(',')]
print(input)
print(min(input), max(input))

def calc_time_to_pos(x: int):
    ret = 0
    for crab in input:
        ret += abs(crab - x)
    return ret

def calc_time_to_pos_pt2(x: int):
    ret = 0
    for crab in input:
        dist = abs(crab - x)
        ret += (dist+1)*dist/2
    return ret

print(min([calc_time_to_pos_pt2(x) for x in range(min(input), max(input) + 1)]))