f = open('d11.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
input = [[int(x) for x in line] for line in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

octopi = input

adj = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]

flashes = 0

# def flash(y, x, orig):
#     global flashes
#     if y < 0 or x < 0 or y >= len(octopi) or x >= len(octopi[0]):
#         return
#     oct = octopi[y][x]
#     # print(oct)
#     if oct == 0:
#         return
#     if not orig:
#         octopi[y][x] += 1
#     if oct > 9:
#         flashes += 1
#         octopi[y][x] = 0
#         for a in adj:
#             flash(y + a[0], x + a[1], orig=False)

sync = False
step = 0
while not sync:
    step += 1
    for y in range(len(octopi)):
        line = octopi[y]
        for x in range(len(line)):
            octopi[y][x] += 1
    mx = max([max(line) for line in octopi])
    while mx > 9:
        for y in range(len(octopi)):
            line = octopi[y]
            for x in range(len(line)):
                if octopi[y][x] > 9:
                    flashes += 1
                    octopi[y][x] = 0
                    for a in adj:
                        y_prime = y + a[0]
                        x_prime = x + a[1]
                        if y_prime < 0 or x_prime < 0 or y_prime >= len(octopi) or x_prime >= len(octopi[0]) or octopi[y_prime][x_prime] == 0:
                            continue
                        else:
                            octopi[y_prime][x_prime] += 1
        mx = max([max(line) for line in octopi])
    if step == 100:
        print("Flashes at step 100: " + str(flashes))
    if mx == 0:
        sync = True

print("Synced at step: " + str(step))
