f = open('d3.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

# positions = [0 for i in range(len(input[0]))]
# total_cnt = len(input)

# for line in input:
#     for i in range(len(line)):
#         if line[i] == '1':
#             positions[i] += 1

# gamma = 0
# epsilon = 0

# power = len(positions)-1
# for i in range(len(positions)):
#     if (positions[i] / total_cnt) < .5:
#         gamma += 2**power
#     else:
#         epsilon += 2**power
#     power -= 1
# print(gamma * epsilon)

all_oxy_possibilities = set(input.copy())
all_scrub_possibilities = set(input.copy())
for i in range(len(input[0])):
    print(all_oxy_possibilities)
    to_remove_scrub = []
    to_remove_oxy = []
    if len(all_scrub_possibilities) > 1:
        positions = 0
        total_cnt = len(all_scrub_possibilities)

        for line in all_scrub_possibilities:
            if line[i] == '1':
                positions += 1
            
        if (positions / total_cnt) >= .5:
            most_common = '1'
        else:
            most_common = '0'

        for line in all_scrub_possibilities:
            if line[i] == most_common:
                to_remove_scrub.append(line)
        for line in to_remove_scrub:
            all_scrub_possibilities.remove(line) 
        
    if len(all_oxy_possibilities) > 1:      
        positions = 0
        total_cnt = len(all_oxy_possibilities)

        for line in all_oxy_possibilities:
            if line[i] == '1':
                positions += 1
            
        if (positions / total_cnt) >= .5:
            most_common = '1'
        else:
            most_common = '0'

        for line in all_oxy_possibilities:
            if line[i] != most_common:
                to_remove_oxy.append(line)
        for line in to_remove_oxy:
            all_oxy_possibilities.remove(line)
    print(all_oxy_possibilities)        

print(all_oxy_possibilities)
print(all_scrub_possibilities)

def convert_to_decimal(bin_num):
    print(bin_num)
    out = 0
    power = len(bin_num)-1
    for i in range(len(bin_num)):
        if int(bin_num[i]) == 1:
            out += 2**power
        power -= 1
    return out

oxy = convert_to_decimal(next(iter(all_oxy_possibilities)))
scrub = convert_to_decimal(next(iter(all_scrub_possibilities)))
print(oxy * scrub)
