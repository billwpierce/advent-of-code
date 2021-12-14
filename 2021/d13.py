f = open('d13.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

x_max = 0
y_max = 0
flips = []
dots = set()
for line in input:
    if line == '':
        continue
    elif line[0] == "f":
        flips.append(line.split("fold along ")[1].split("="))
    else:
        x, y = [int(x) for x in line.split(",")]
        x_max = max(x, x_max)
        y_max = max(y, y_max)
        dots.add((x, y))

def do_flip(flip):
    if flip[0] == 'x':
        do_horizontal_flip(int(flip[1]))
    else:
        do_vertical_flip(int(flip[1]))

def do_horizontal_flip(x_pos):
    global x_max
    global dots
    dots_prime = set()
    for dot in dots:
        dot_x, dot_y = dot
        if dot_x > x_pos:
            new_x = x_pos - (dot_x - x_pos)
        else:
            new_x = dot_x
        dots_prime.add((new_x, dot_y))
    x_max = x_pos - 1
    dots = dots_prime

def do_vertical_flip(y_pos):
    global y_max
    global dots
    dots_prime = set()
    for dot in dots:
        dot_x, dot_y = dot
        if dot_y > y_pos:
            new_y = y_pos - (dot_y - y_pos)
        else:
            new_y = dot_y
        dots_prime.add((dot_x, new_y))
    y_max = y_pos - 1
    dots = dots_prime

def visualize():
    global dots
    global x_max, y_max
    map = [['.' for x in range(x_max+1)] for y in range(y_max+1)]
    for dot in dots:
        x, y = dot
        map[y][x] = "#"
    for line in map:
        print(''.join(line))

for flip in flips:
    do_flip(flip)
visualize()
print(len(dots))