f = open('d10.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

## Part 1
error = 0

open_to_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
close_to_open = {"(": ")", "[": "]", "{": "}", "<": ">"}
error_convert = {")": 3, "]": 57, "}": 1197, ">": 25137}

for line in input:
    openers = []
    for c in line:
        if c in "([{<":
            openers.append(c)
        else:
            if open_to_close[openers.pop()] != c:
                error += error_convert[c]
                break
                

print(error)


## Part 2

incomplete = []

open_to_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
error_convert = {")": 3, "]": 57, "}": 1197, ">": 25137}
autocomplete = {")": 1, "]": 2, "}": 3, ">": 4}

scores = []

for line in input:
    score = 0
    openers = []
    corrupt = False
    for c in line:
        if c in "([{<":
            openers.append(c)
        else:
            if open_to_close[openers.pop()] != c:
                corrupt = True
                break
    if not corrupt:
        openers.reverse()
        for c in openers:
            score *= 5
            score += autocomplete[open_to_close[c]]
        scores.append(score)
                
# print(scores)
print(sorted(scores)[len(scores) // 2])
