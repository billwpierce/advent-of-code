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

def game(p1deck, p2deck):
    cache = []
    while min(len(p1deck), len(p2deck)) != 0:
        # print(p1deck, p2deck)
        stringify = str(p1deck) + "|" + str(p2deck)
        if stringify in cache:
            return True
        else:
            cache.append(stringify)
        p1card = p1deck[0]
        p2card = p2deck[0]
        p1deck.pop(0)
        p2deck.pop(0)
        if len(p1deck) >= p1card and len(p2deck) >= p2card:
            call = game(p1deck[:p1card].copy(), p2deck[:p2card].copy())
            if call:
                p1deck.extend([p1card, p2card])
            else:
                p2deck.extend([p2card, p1card])
        else:
            if p1card > p2card:
                p1deck.extend([p1card, p2card])
            elif p2card > p1card:
                p2deck.extend([p2card, p1card])
    if len(p1deck) == 0:
        return False
    else:
        return True

game(player_1_deck, player_2_deck)

print(player_1_deck)
print(player_2_deck)

sm = 0
for i in range(len(player_1_deck)):
    sm += (i+1)*player_1_deck[len(player_1_deck)-i-1]

print("p1", sm)

sm = 0
for i in range(len(player_2_deck)):
    sm += (i+1)*player_2_deck[len(player_2_deck)-i-1]

print("p2", sm)