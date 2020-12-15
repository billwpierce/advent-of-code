f = open('in15.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
input = [int(x) for x in input[0].split(",")]
print(input)

spoken = input.copy()

mxn = {}
tmp = {}
num_cnt = {}

# num_to_print = 2020 # Part 1
num_to_print = 30000000 # Part 2

for i in range(num_to_print):
    if i in range(len(input)):
        num_cnt[spoken[i]] = 1
        tmp[spoken[i]] = i
        pass
    else:
        if num_cnt[spoken[i-1]] == 1:
            spoken.append(0)
            num_cnt[0] += 1
            mxn[0] = tmp[0]
            tmp[0] = i
        else:
            spoken.append((i-1) - mxn[spoken[i-1]])
            if spoken[i] in tmp:
                mxn[spoken[i]] = tmp[spoken[i]]
            tmp[spoken[i]] = i
            if not spoken[i] in num_cnt:
                num_cnt[spoken[i]] = 0
            num_cnt[spoken[i]] += 1
            
print(spoken[num_to_print-1])