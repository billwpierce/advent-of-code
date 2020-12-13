f = open('in13.txt', 'r') # Insert the correct day
# # Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # @d array of the input

earliest_time = int(input[0])
buses = input[1].split(",")

def is_divisible(num1, num2):
    return num1 % num2 == 0

# Part 1

def part1():
    i = earliest_time
    while True:
        for bus in buses:
            if bus == "x":
                pass
            else:
                if is_divisible(i, int(bus)):
                    return int(bus) * (i - earliest_time)
        i += 1

print(part1())

# Part 2

test = {k:int(buses[k]) for k in range(len(buses)) if buses[k] != "x"}

from math import gcd

def lcm(a): # https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
    lcmc = a[0]
    for i in a[1:]:
        lcmc = lcmc*i//gcd(lcmc, i)
    return lcmc

def part2():
    i = 0
    def helper(i):
        acceptables = [1]
        for j, num in test.items():
            if not is_divisible(i + j, num):
                return (False, lcm(acceptables))
            else:
                acceptables.append(num)
        return (True, -1)
    while True:
        temp = helper(i)
        if temp[0]:
            return i
        else:
            i += temp[1]
        
print(part2())
