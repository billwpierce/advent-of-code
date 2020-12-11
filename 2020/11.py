f = open('in11.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
input = [[x for x in line] for line in input]

# print(input)
mnx = 0
mxx = len(input[0]) - 1
mny = 0
mxy = len(input) - 1

def get_seat(array, x, y):
    return array[y][x]

# Part 1

def adjacents(x, y, array):
    rets = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1), (x+1, y-1), (x+1, y), (x+1, y+1)]
    ret = ""
    for r in rets:
        if r[0] >= mnx and r[0] <= mxx and r[1] >= mny and r[1] <= mxy:
            ret += get_seat(array, r[0], r[1])
    return ret

def iterateo(input):
    old = [line.copy() for line in input]
    new = [line.copy() for line in input]
    while True:
        changes = 0
        for y in range(len(old)):
            for x in range(len(old[y])):
                num_occ = sum([1 for i in adjacents(x, y, old) if i == "#"])
                st = get_seat(old, x, y)
                if st == "L" and num_occ == 0:
                    changes += 1
                    new[y][x] = "#"
                elif st == "#" and num_occ >= 4:
                    changes += 1
                    new[y][x] = "L"
        if changes == 0:
            return new
        old = [line.copy() for line in new]

def count_occupied(res):
    num_occ = 0
    for line in res:
        for c in line:
            if c == "#":
                num_occ += 1
    return num_occ

print(count_occupied(iterateo(input)))

# Part 2

def count_visible_occupied(array, stx, sty):
    def helper(x, y, dirx, diry):
        if x < mnx or y < mny or x > mxx or y > mxy or get_seat(array, x, y) == "L":
            return 0
        elif get_seat(array, x, y) == "#":
            return 1
        else:
            return helper(x + dirx, y + diry, dirx, diry)
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum([helper(stx + dirx, sty + diry, dirx, diry) for dirx, diry in dirs])

def lineofsight(input):
    old = [line.copy() for line in input]
    new = [line.copy() for line in input]
    while True:
        changes = 0
        for y in range(len(old)):
            for x in range(len(old[y])):
                num_occ = count_visible_occupied(old, x, y)
                st = get_seat(old, x, y)
                if st == "L" and num_occ == 0:
                    changes += 1
                    new[y][x] = "#"
                elif st == "#" and num_occ >= 5:
                    changes += 1
                    new[y][x] = "L"
        if changes == 0:
            return new
        old = [line.copy() for line in new]

print(count_occupied(lineofsight(input)))