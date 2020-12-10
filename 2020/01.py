original_input = open('in01.txt', 'r') 
all_lines = original_input.readlines() 

print(all_lines)

for line1 in all_lines:
    val1 = int(line1)
    for line2 in all_lines:
        val2 = int(line2)
        if (str(2020-val1-val2) + "\n") in all_lines:
            print(val1 * val2 * (2020-val1-val2))