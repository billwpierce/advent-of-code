import itertools

f = open('d8.txt', 'r') # Insert the correct day
# f = open('d8test.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

# input = [line.split(" | ") for line in input]
# cnt = 0
# for line in input:
#     # print(line[1])
#     for out in line[1].split():
#         if len(out) in [2, 4, 3, 7]:
#             # print(out)
#             cnt += 1
# print(cnt)

chars = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def calculate_universal(inputs):
    for perm in list(itertools.permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g',])):
        works = True
        dct = {'a': perm[0], 'b': perm[1], 'c': perm[2], 'd': perm[3], 'e': perm[4], 'f': perm[5], 'g': perm[6]}
        for inp in inputs:
            new_str = ''
            for char in inp:
                new_str += dct[char]
            new_str = "".join(sorted(new_str))
            if not new_str in chars:
                works = False
                break
        if works:
            return dct

input = [line.split(" | ") for line in input]
cnt = 0
sm = 0
for line in input:
    new_summand = ''
    universal = calculate_universal(line[0].split())
    for out in line[1].split():
        new_str = ''
        for char in out:
            new_str += universal[char]
        new_str = "".join(sorted(new_str))
        new_summand += str(chars.index(new_str))
    sm += int(new_summand)
print(sm)


