original_input = open('day7input.txt', 'r') 
all_lines = original_input.readlines()

def RepresentsInt(s): # https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
    try: 
        int(s)
        return True
    except ValueError:
        return False

#Part 1

containers = {}

for line in all_lines:
    split_space = line.split(" ")
    bag_name = split_space[0] + " " + split_space[1]
    for i in range(len(split_space)):
        if RepresentsInt(split_space[i]):
            new_bag_name = split_space[i+1] + " " + split_space[i + 2]
            add_to_container(new_bag_name, bag_name)

contains_sg = []

outer_dict = containers["shiny gold"].copy()

def helper(lst):
    for elem in lst:
        if not(elem in contains_sg):
            contains_sg.append(elem)
            if elem in containers:
                helper(containers[elem])

helper(outer_dict)

print(len(set(contains_sg)))
print(contains_sg)

# Part 2

containers = {}

def add_to_container(cnt_name, val, cnt):
    if cnt_name in containers.keys():
        containers[cnt_name].append([val, cnt])
    else:
        containers[cnt_name] = [[val, cnt]]

for line in all_lines:
    split_space = line.split(" ")
    bag_name = split_space[0] + " " + split_space[1]
    for i in range(len(split_space)):
        if RepresentsInt(split_space[i]):
            num = split_space[i]
            new_bag_name = split_space[i+1] + " " + split_space[i + 2]
            add_to_container(bag_name, new_bag_name, num)

outer_dict = containers["shiny gold"].copy()

def helper_two(lst):
    print(lst)
    sumt = 0
    for elem in lst:
        sumt += int(elem[1])
        if elem[0] in containers:
            print(elem[0])
            sumt += int(elem[1]) * helper(containers[elem[0]])
    return sumt

print(helper_two(outer_dict))

