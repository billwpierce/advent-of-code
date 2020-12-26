f = open('in25.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

card_public_key = 19241437
door_public_key = 17346587

# card_public_key = 5764801
# door_public_key = 17807724

val = 1
cnt_card = 0
while val != card_public_key:
    cnt_card += 1
    val = (val*7) % 20201227

print(cnt_card)

val = 1
cnt_door = 0
while val != door_public_key:
    cnt_door += 1
    val = (val*7) % 20201227

print(cnt_door)

val = 1
for i in range(cnt_card):
    val = (val*door_public_key) % 20201227

print(val)

val = 1
for i in range(cnt_door):
    val = (val*card_public_key) % 20201227

print(val)