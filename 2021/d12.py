f = open('d12.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

vertices = set()
edges = {}

for line in input:
    v1, v2 = line.split("-")
    vertices.add(v1)
    vertices.add(v2)
    if v1 not in edges:
        edges[v1] = [v2]
    else:
        edges[v1].append(v2)
    if v2 not in edges:
        edges[v2] = [v1]
    else:
        edges[v2].append(v1)

# def is_lower_revisit(prefix):
#     at_least_one = set()
#     for i in prefix:
#         if i[0].islower():
#             if i in at_least_one:
#                 return True
#             else:
#                 at_least_one.add(i)
#     return False

# def helper(prefix, curr_el):
#     # from the path at curr_el with previous elements prefix, output
#     # the number of paths to end that only go through one lowercase.
#     if is_lower_revisit(prefix):
#         return 0
#     if curr_el == 'end':
#         print(prefix)
#         return 1
#     cnt = 0
#     for out in edges[curr_el]:
#         cnt += helper(prefix + [out], out)
#     return cnt

# print(helper(["start"], "start"))

def is_lower_revisit(prefix):
    cnts = {v:0 for v in vertices if v[0].islower()}
    num_at_two = set()
    for i in prefix:
        if i[0].islower():
            cnts[i] += 1
            if i in ["start", "end"] and cnts[i] > 1:
                return True
            if cnts[i] == 2:
                num_at_two.add(i)
            if len(num_at_two) > 1:
                return True
            if cnts[i] > 2:
                return True
    return False

def helper(prefix, curr_el):
    # from the path at curr_el with previous elements prefix, output
    # the number of paths to end that only go through one lowercase.
    if is_lower_revisit(prefix):
        return 0
    if curr_el == 'end':
        print(prefix)
        return 1
    cnt = 0
    for out in edges[curr_el]:
        cnt += helper(prefix + [out], out)
    return cnt

print(helper(["start"], "start"))