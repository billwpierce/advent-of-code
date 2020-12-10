original_input = open('day3input.txt', 'r') 
all_lines = original_input.readlines() 

# wraparound_x = len(all_lines[0])
wraparound_x = 31
max_y = len(all_lines)

def get_location(x, y):
    if y >= max_y:
        return "-"
    return all_lines[y][x % (wraparound_x)]

# print(get_location(3, 1))
# print(wraparound_x)
# print(max_y)

def num_trees(r, d):
    counter = 0
    x, y = 0, 0
    while True:
        x, y = x+r, y+d
        get_loc = get_location(x, y)
        if get_loc == "-":
            break
        elif get_loc == "#":
            counter += 1
    return counter

print(num_trees(1, 1) * num_trees(3, 1) * num_trees(5, 1) * num_trees(7, 1) * num_trees(1, 2))

print(num_trees(3, 1))