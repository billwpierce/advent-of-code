f = open('in21.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

# print(input)

ati = {}
all_ingredients = []

for line in input:
    allergens = line.split(" (contains ")[1].split(", ")
    allergens[-1] = allergens[-1].replace(")", "")
    ingredients = line.split(" (contains ")[0].split(" ")
    for a in allergens:
        if a in ati:
            ati[a] = list(filter(lambda x: x in ingredients, ati[a]))
        else:
            ati[a] = ingredients
    all_ingredients.extend(ingredients)

for key, value in ati.items():
    all_ingredients = list(filter(lambda x: x not in value, all_ingredients))

# Part 1
print(len(all_ingredients))

final = {}
s = 0
while s < len(ati.keys()):
    s = 0
    for key in ati.keys():
        if len(ati[key]) == 1:
            final[key] = ati[key]
            for new_key in ati.keys():
                if new_key != key:
                    try:
                        ati[new_key].remove(ati[key][0])
                    except:
                        pass
            s += 1

sortednames=sorted(final.keys(), key=lambda x:x.lower())
out = ""
for name in sortednames:
    out += final[name][0]
    out += ","

# Part 2
print(out)