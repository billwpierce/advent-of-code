f = open('in23.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

cups = [6, 4, 3, 7, 1, 9, 2, 5, 8]
# cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]
# curr_index = 0

for i in range(100):
    curr_cup = cups[0]
    pud = []
    for j in range(3):
        pud.append(cups.pop(1))
    dest_label = curr_cup - 1
    while not dest_label in cups:
        dest_label -= 1
        if dest_label < min(cups):
            dest_label = max(cups)
    if dest_label == curr_cup:
        raise Exception("what")
    new_ind = cups.index(dest_label)
    incr = 1
    for j in range(3):
        pos = new_ind+incr+j
        cups.insert((new_ind+incr+j)%10, pud[j])
    temp = cups.pop(0)
    cups.append(temp)

print(cups)
#[3, 2, 6, 1, 4, 5, 9, 8, 7]
# 45987326