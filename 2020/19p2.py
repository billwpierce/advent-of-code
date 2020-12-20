import functools
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

update_8_and_11 = False
if update_8_and_11:
    rules.append("8: 42 | 42 8")
    rules.append("11: 42 31 | 42 11 31")

ruleset = {}

for rule in rules:
    key = int(rule.split(":")[0])
    if key == 24:
        ruleval = "b"
    elif key == 36:
        ruleval = "a"
    # if key == 14:
    #     ruleval = "b"
    # elif key == 1:
    #     ruleval = "a"
    else:
        ruleval = [[int(i) for i in x.split(" ") if i != ""] for x in rule.split(":")[1].split("|")]
    ruleset[key] = ruleval

def generate_from_rule(rule, max_len=0):
    if max_len <= 0:
        # print("gone")
        return [""]
    if type(rule) is str:
        return [rule]
    elif type(rule[0]) == list:
        messages = []
        for i in rule:
            messages.extend(generate_from_rule(i, max_len))
        return messages
    elif type(rule) == list:
        messages = []
        for index in rule:
            if messages == []:
                messages = generate_from_rule(ruleset[index], max_len)
            else:
                temp = []
                for m in messages: # For every message we have so far
                    temp.extend([m + g for g in generate_from_rule(ruleset[index], max_len-len(m))])
                messages = temp
        return messages
    else:
        raise Exception("what")

g42 = generate_from_rule(ruleset[42], 1000)
g31 = generate_from_rule(ruleset[31], 1000)

def fancy_checker(message):
    if len(message) % 8 != 0:
        return False
    c = 42
    c31 = 0
    c42 = 0
    for i in range(len(message) // 8):
        if c == 42:
            if not message[8*i:8*(i+1)] in g42:
                c = 31
                if not message[8*i:8*(i+1)] in g31:
                    return False
                else:
                    c31 += 1
                continue
            else:
                c42 += 1
        elif c == 31:
            if not message[8*i:8*(i+1)] in g31:
                return False
            else:
                c31 += 1
        else:
            raise Exception("What", message, i)
    if (c42 - c31) >= 1 and c31 >= 1:
        return True
    else:
        return False

sm = 0
for m in messages:
    if fancy_checker(m):
        sm += 1

print(sm)