original_input = open('day9input.txt', 'r') 
all_lines = original_input.readlines()

# Part 1

def helper(prm):
    for i in range(prm, len(all_lines)):
        safe = False
        for j in range(1, prm):
            num_needed = int(all_lines[i]) - int(all_lines[i-j])
            if str(num_needed)+"\n" in all_lines[i-prm:i]:
                safe = True
                break
        if not safe:
            return int(all_lines[i])
        

print(helper(25))

# Part 2

weakness = helper(25)

def find_cont_sum(val):
    def attempt_sum(min_val, max_val, curr_sum, next_index):
        new_val = int(all_lines[next_index])
        summed = curr_sum + new_val
        if new_val < min_val:
            min_val = new_val
        if new_val > max_val:
            max_val = new_val
        if summed > val:
            return False, -1, -1
        elif summed == val:
            return True, min_val, max_val
        else:
            return attempt_sum(min_val, max_val, summed, next_index + 1)
    for i in range(len(all_lines)):
        atmp = attempt_sum(int(all_lines[i]), int(all_lines[i]), int(all_lines[i]), i+1)
        if atmp[0]:
            return atmp[1] + atmp[2]

print(find_cont_sum(weakness))