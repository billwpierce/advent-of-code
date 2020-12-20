f = open('in19.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
# input = f.read().splitlines()  # Raw Reading
input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
input = [x.split("\n") for x in input]

rules = input[0]
messages = input[1]

ruleset = {}

for rule in rules:
    key = int(rule.split(":")[0])
    if key == 24:
        ruleval = "b"
    elif key == 36:
        ruleval = "a"
    # if key == 5:
    #     ruleval = "b"
    # elif key == 4:
    #     ruleval = "a"
    else:
        ruleval = [[int(i) for i in x.split(" ") if i != ""] for x in rule.split(":")[1].split("|")]
    ruleset[key] = ruleval

def check_against_rule(rule, message):
    # print(rule, message)
    if type(rule) is str:
        if rule == message[0]:
            return (True, message[1:])
        else:
            return (False, "")
    elif type(rule[0]) == list:
        for i in range(len(rule)):
            temp = check_against_rule(rule[i], message)
            if temp[0]:
                return (True, temp[1])
        return (False, "")
    elif type(rule) == list:
        m = message
        for r in rule:
            temp = check_against_rule(ruleset[r], m)
            if temp[0] == False:
                return (False, "")
            m = temp[1]
        return (True, m)
    else:
        raise Exception("what")

def check_rule_index(index, message):
    out = check_against_rule(ruleset[index], message)
    if out[0] == True and out[1] == "":
        return True
    else:
        return False

sm = 0
for m in messages:
    if check_rule_index(0, m):
        sm += 1

print(sm)