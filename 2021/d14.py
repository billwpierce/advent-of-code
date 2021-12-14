f = open('d14.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

polymer = input[0]

rules = {}
for rule in input[2:]:
    pair, insert = rule.split(" -> ")
    rules[pair] = insert

# Part 1
for step in range(10):
    new_polymer = ''
    for i in range(len(polymer) - 1):
        new_polymer += polymer[i]
        new_polymer += rules[polymer[i:i+2]]
    new_polymer += polymer[len(polymer)-1]
    polymer = new_polymer

counts = {}
for char in polymer:
    if char not in counts:
        counts[char] = 0
    counts[char] += 1

print(max(counts.values()) - min(counts.values()))

# Part 2
poly_counts = {}
for poly in rules:
    polymer = poly
    for step in range(20):
        new_polymer = ''
        for i in range(len(polymer) - 1):
            new_polymer += polymer[i]
            new_polymer += rules[polymer[i:i+2]]
        new_polymer += polymer[len(polymer)-1]
        polymer = new_polymer
    counts = {}
    for char in polymer:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    poly_counts[poly] = counts
    print(counts)

polymer = input[0]
for step in range(20):
    new_polymer = ''
    for i in range(len(polymer) - 1):
        new_polymer += polymer[i]
        new_polymer += rules[polymer[i:i+2]]
    new_polymer += polymer[len(polymer)-1]
    polymer = new_polymer

counts = {}
for i in range(len(polymer) - 1):
    pcs = poly_counts[polymer[i:i+2]]
    for key in pcs:
        value = pcs[key]
        if key not in counts:
            counts[key] = 0
        counts[key] += value

for char in polymer[:-1]:
    counts[char] -= 1

print(max(counts.values()) - min(counts.values()))
print(counts)
