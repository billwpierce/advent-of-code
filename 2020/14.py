f = open('in14.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # @d array of the input

# Part 1

mask = {}
memory = {}

def update_mask(new_mask_st):
    msk = {}
    new_mask_st = new_mask_st[::-1]
    for i in range(len(new_mask_st)):
        if new_mask_st[i] == "1" or new_mask_st[i] == "0":
            msk[i] = int(new_mask_st[i])
        else:
            msk[i] = new_mask_st[i]
    return msk

def int_to_bin(integer):
    bina = {}
    for i in range(36):
        bina[i] = integer % 2
        integer = integer // 2
    return bina

def apply_mask(mask, number):
    bn = int_to_bin(number)
    output = {}
    for i in range(36):
        if mask[i] == "X":
            output[i] = bn[i]
        else:
            output[i] = mask[i]
    return sum([(2 ** key)*val for key, val in output.items()])

for line in input:
    if line[:2] == "ma":
        mask = update_mask(line.split('= ')[1])
    else:
        ind = int(line.split('[')[1].split(']')[0])
        val = int(line.split('=')[1])
        memory[ind] = apply_mask(mask, val)

def part1():
    return sum([val for val in memory.values()])

print(part1())

# Part 2

mask = {}
memory = {}

def apply_mask_v2(mask, mem_loc):
    bn = int_to_bin(mem_loc)
    output = {}
    num_floating = 0
    for i in range(36):
        if mask[i] == 0:
            output[i] = bn[i]
        elif mask[i] == 1:
            output[i] = 1
        else: # = X
            output[i] = "X"
            num_floating += 1
    def helper(base, i):
        if i >= len(base):
            return [{}]
        elif base[i] == "X":
            ret = []
            for res in helper(base, i+1):
                r0 = res.copy()
                r0[i] = 0
                r1 = res.copy()
                r1[i] = 1
                ret.append(r0)
                ret.append(r1)
            return ret
        else:
            ret = []
            for res in helper(base, i+1):
                res[i] = base[i]
                ret.append(res)
            return ret
    return helper(output, 0)

for line in input:
    if line[:2] == "ma":
        mask = update_mask(line.split('= ')[1])
    else:
        ind = int(line.split('[')[1].split(']')[0])
        val = int(line.split('=')[1])
        msk = apply_mask_v2(mask, ind)
        for mem in msk:
            mn = sum([(2 ** key)*val for key, val in mem.items()])
            memory[mn] = val

def part2():
    return sum([val for val in memory.values()])

print(part2())