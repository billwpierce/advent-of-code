f = open('d1.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

i = 0
x_prev = 0
for x in input:
    if x == input[0]:
        x_prev = x
    else:
        if x > x_prev:
            i += 1
        x_prev = x
print(i)

i = 0
x_prev = 0
curr = 0
j = 0
for x in range(len(input)):
    if x <= 2:
        pass
    else:
        if input[x] > input[x-3]:
            i += 1
print(i)