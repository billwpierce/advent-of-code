f = open('in22.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
input = [x.split("\n") for x in input]

print(input)

player_1_deck = []
player_2_deck = []
curr_deck = player_1_deck
for i in input:
    val = i[0]
    if val == "Player 1:":
        continue
    elif val == "Player 2:":
        curr_deck = player_2_deck
        continue
    else:
        if val != "":
            curr_deck.append(int(val))

print(player_1_deck)
print(player_2_deck)

while min(len(player_1_deck), len(player_2_deck)) != 0:
    p1card = player_1_deck[0]
    p2card = player_2_deck[0]
    if p1card > p2card:
        player_1_deck.extend([p1card, p2card])
    elif p2card > p1card:
        player_2_deck.extend([p2card, p1card])
    player_2_deck.pop(0)
    player_1_deck.pop(0)

print(player_1_deck)
print(player_2_deck)

sm = 0
for i in range(len(player_2_deck)):
    sm += (i+1)*player_2_deck[len(player_2_deck)-i-1]

print(sm)