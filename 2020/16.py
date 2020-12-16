f = open('in16.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
# input = f.read().splitlines()  # Raw Reading
input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
input = [x.split("\n") for x in input]
# print(input[0])
rules = input[0]
tickets = input[2][1:]
valid_ranges = []

part = 2

# Part 1
if part == 1:
    for rule in rules:
        ranges = [x.split("-") for x in rule.split(": ")[1].split(" or ")]
        valid_ranges.append(range(int(ranges[0][0]), int(ranges[0][1])+1))
        valid_ranges.append(range(int(ranges[1][0]), int(ranges[1][1])+1))

    rej_val = 0

    for ticket in tickets:
        vals = [int(x) for x in ticket.split(",")]
        for val in vals:
            rej_val += val
            for rng in valid_ranges:
                if val in rng:
                    rej_val -= val
                    break

    print(rej_val)

# Part 2
if part == 2:
    for rule in rules:
        ranges = [x.split("-") for x in rule.split(": ")[1].split(" or ")]
        valid_ranges.append(range(int(ranges[0][0]), int(ranges[0][1])+1))
        valid_ranges.append(range(int(ranges[1][0]), int(ranges[1][1])+1))

    valid_tickets = []

    for ticket in tickets:
        vals = [int(x) for x in ticket.split(",")]
        valid_ = True
        for val in vals:
            this_val_valid = False
            for rng in valid_ranges:
                if val in rng:
                    this_val_valid = True
                    break
            if not this_val_valid:
                valid_ = False
                break
        if valid_ == True:
            valid_tickets.append(ticket)

    valid_tickets.append(input[1][1])

    valid_ranges = {input[0][i//2].split(":")[0]:(valid_ranges[i], valid_ranges[i+1]) for i in range(len(valid_ranges)) if i % 2 == 0}

    columns = []

    for i in range(len(valid_tickets[0].split(","))):
        columns.append([int(ticket.split(",")[i]) for ticket in valid_tickets])

    workable_columns = {}

    for key, values in valid_ranges.items():
        workable_columns[key] = []
        for col in columns:
            addable = True
            for val in col:
                if not(val in values[0] or val in values[1]):
                    addable = False
                    break
            if addable:
                workable_columns[key].append(col)

    possible_names = [[] for _ in range(len(columns))]

    for key, values in valid_ranges.items():
        for i in range(len(columns)):
            addable = True
            for val in columns[i]:
                if not(val in values[0] or val in values[1]):
                    addable = False
                    break
            if addable:
                possible_names[i].append(key)

    actual_columns = {}
    mx = 0
    while mx < len(possible_names):
        mx = 0
        for j in range(len(possible_names)):
            name = possible_names[j]
            if len(name) == 1:
                mx += 1
                for i in range(len(possible_names)):
                    if not possible_names[i] == name and name[0] in possible_names[i]:
                        possible_names[i].remove(name[0])
                actual_columns[name[0]] = columns[j]

    my_ticket_index = len(valid_tickets) - 1

    sm = 1
    for key in actual_columns.keys():
        for val in actual_columns[key]:
            assert val in valid_ranges[key][0] or val in valid_ranges[key][1], val + " falls outside of " + key
        if key.split(" ")[0] == "departure":
            print(key)
            print(actual_columns[key][my_ticket_index])
            sm = sm * actual_columns[key][my_ticket_index]

    print(sm)
