f = open('day10input.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces

# Part 1

print(input)

def helper(curr, lst):
    if curr+1 in lst:
        tmp = helper(curr+1, lst)
        tmp[0] = tmp[0] + 1
        return tmp
    if curr+2 in lst:
        tmp = helper(curr+2, lst)
        tmp[1] = tmp[1] + 1
        return tmp
    if curr+3 in lst:
        tmp = helper(curr+3, lst)
        tmp[2] = tmp[2] + 1
        return tmp
    return [0, 0, 0]

print(helper(0, input + [max(input) + 3]))

# Part 2

solved = {}
solved[0] = 1

def another_one(curr, lst):
    if curr in solved:
        return solved[curr]
    elif not curr in lst:
        return 0
    else:
        tmp = another_one(curr - 1, lst) + another_one(curr - 2, lst) + another_one(curr - 3, lst)
        solved[curr] = tmp
        return tmp

print(another_one(max(input), input))