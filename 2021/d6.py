## Part 1

f = open('d6.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

fishes = [int(x) for x in input[0].split(',')]
# print(fishes)

for day in range(80):
    if day < 10:
        print(len(fishes))
    for f in range(len(fishes)):
        fish = fishes[f]
        if fish == 0:
            fishes[f] = 6
            fishes.append(8)
        else:
            fishes[f] -= 1

print(len(fishes))


# Part 2

f = open('d6.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

fishes = [int(x) for x in input[0].split(',')]
incrementers = [0 for i in range(7)]
skip_crementers = [0 for i in range(7)]
fish_count = len(fishes)
# print(fishes)

for f in range(len(fishes)):
    incrementers[fishes[f]] += 1

# print(incrementers)
# print(skip_crementers)

for day in range(256):
    incrs = incrementers[day % 7]
    fish_count += incrs
    skip_crementers[(day+2) % 7] = incrs
    incrementers[day % 7] += skip_crementers[day % 7]
    skip_crementers[day % 7] = 0


print(fish_count)
print(incrementers)
print(skip_crementers)