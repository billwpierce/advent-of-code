original_input = open('day6testinput.txt', 'r') 
all_lines = original_input.readlines()

# Part 2 Attempt 1

# index = 0
# valid_chars = [c for c in all_lines[0]]
# valid_chars.remove("\n")
# counter = 0
# print(valid_chars)

# for i in range(len(all_lines)):
#     if all_lines[i] == "\n":
#         counter += len(valid_chars)
#         valid_chars = [c for c in all_lines[i + 1]]
#         valid_chars.remove("\n")
#     else:
#         for c in valid_chars:
#             if not(c in all_lines[i]):
#                 valid_chars.remove(c)

# counter += len(valid_chars)

# print(counter)

# Part 2 Attempt 2

ind = 0
yesses = [[]]
new_group = True
cl = []

for line in all_lines:
    if line == "\n":
        cl.append(len(yesses[ind]))
        ind += 1
        yesses.append([])
        new_group = True
    else:
        if new_group:
            for c in line:
                if not (c == "\n"):
                    yesses[ind].append(c)
            new_group = False
        else:
            print(line)
            print(yesses[ind])
            for c in yesses[ind]:
                print(c)
                if not(c in line):
                    yesses[ind].remove(c)
                    print(yesses[ind])

cl.append(len(yesses[ind]))

count = 0
for i in range(len(yesses)):
    yesses[i] = set(yesses[i])
    count += len(yesses[i])

print(yesses)
# print(count)
print(cl)
# print(sum(cl))

# Part 2 Attempt 3

ci = 0
list_of_groups = [[]]

for line in all_lines:
    if line == "\n":
        ci += 1
        list_of_groups.append([])
    else:
        list_of_groups[ci].append(line.split("\n")[0])
        # list_of_groups[ci].remove("\n")

# print(list_of_groups)

counter = 0
prev = 0
counters = []
for group in list_of_groups:
    for char in "abcdefghijklmnopqrstuvwxyz":
        ng = 0
        for person in group:
            if char in person:
                ng += 1
        if ng == len(group):
            counter += 1
    counters.append(counter - prev)
    prev = counter

print(counter)
print(counters)
        