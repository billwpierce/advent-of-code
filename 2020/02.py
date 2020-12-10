original_input = open('day2input.txt', 'r') 
total_passwords = original_input.readlines() 

part_1_valid = 0

for line in total_passwords:
    bits = line.split(" ")
    range_ = bits[0].split("-")
    prot_char = bits[1][0]
    password = bits[2]
    count_prot = 0
    for char in password:
        if char == prot_char:
            count_prot += 1
    if count_prot >= int(range_[0]) and count_prot <= int(range_[1]):
        part_1_valid += 1

print(part_1_valid)

part_2_valid = 0

for line in total_passwords:
    bits = line.split(" ")
    locs = bits[0].split("-")
    prot_char = bits[1][0]
    password = bits[2]
    if (password[int(locs[0]) - 1] == prot_char) != (password[int(locs[1]) - 1] == prot_char):
        part_2_valid += 1

print(part_2_valid)