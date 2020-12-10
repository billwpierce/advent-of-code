original_input = open('in08.txt', 'r') 
all_lines = original_input.readlines()

commands_one = []
for line in all_lines:
    cmd = line[:3]
    num = int(line[4:])
    commands_one.append((cmd, num, 0))

commands_two = []
for line in all_lines:
    cmd = line[:3]
    num = int(line[4:])
    commands_two.append((cmd, num, 0))

def helper(cmds, pos):
    if pos >= len(cmds):
        return [0, True]
    tpl = cmds[pos]
    if tpl[2] >= 1:
        return [0, False]
    cmd = tpl[0]
    num = tpl[1]
    cmds[pos] = (cmd, num, tpl[2] + 1)
    if cmd == "acc":
        tmp = helper(cmds, pos + 1)
        return [num + tmp[0], tmp[1]]
    elif cmd == "jmp":
        return helper(cmds, pos + num)
    elif cmd == "nop":
        return helper(cmds, pos + 1)

# Part 1
print(helper(commands_one, 0))

# Part 2
for i in range(len(all_lines)):
    if commands_two[i][0] == "acc":
        pass
    else:
        tmp_cmds = commands_two.copy()
        if tmp_cmds[i][0] == "jmp":
            tmp_cmds[i] = ("nop", tmp_cmds[i][1], tmp_cmds[i][2])
        else:
            tmp_cmds[i] = ("jmp", tmp_cmds[i][1], tmp_cmds[i][2])
        res = helper(tmp_cmds, 0)
        if res[1] == True:
            print(res)
        else:
            pass