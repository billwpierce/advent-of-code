original_input = open('in04.txt', 'r') 
all_lines = original_input.readlines() 

ind = 0
passports = [{}]

for line in all_lines:
    if line == "\n":
        ind += 1
        passports.append({})
    else:
        pairs = [pair.split(":") for pair in line.split(" ")]
        for pair in pairs:
            key = pair[0]
            val = pair[1]
            if "\n" in val:
                passports[ind][key] = val[:-1]
            else:
                passports[ind][key] = val

valid_ports = []

for port in passports:
    if len(port.keys()) == 8:
        valid_ports.append(port)
    else:
        if not ("cid" in port.keys()) and len(port.keys()) == 7:
            valid_ports.append(port)

print(len(valid_ports))
print(len(passports))

def validate_hex(hex_str):
    for c in hex_str:
        if not (c in "0123456789abcdef"):
            return False
    return True

def RepresentsInt(s): # https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
    try: 
        int(s)
        return True
    except ValueError:
        return False

def validate_port(pp):
    if not(len(pp['byr']) == 4 and int(pp['byr']) >= 1920 and int(pp['byr']) <= 2002):
        print("byr:" + str(pp))
        return False
    if not(len(pp['iyr']) == 4 and int(pp['iyr']) >= 2010 and int(pp['iyr']) <= 2020):
        print("iyr:" + str(pp))
        return False
    if not(len(pp['eyr']) == 4 and int(pp['eyr']) >= 2020 and int(pp['eyr']) <= 2030):
        print("eyr:" + str(pp))
        return False
    if not((pp['hgt'][-2:] == "cm" or pp['hgt'][-2:] == "in") and RepresentsInt(pp['hgt'][:-2])):
        print("hgt:" + str(pp))
        return False
    if not((pp['hgt'][-2:] == "cm" and int(pp['hgt'][:-2]) >= 150 and int(pp['hgt'][:-2]) <= 193) or (pp['hgt'][-2:] == "in" and int(pp['hgt'][:-2]) >= 59 and int(pp['hgt'][:-2]) <= 76)):
        print("hgt2:" + str(pp))
        return False
    if not(pp['hcl'][0] == "#" and len(pp['hcl']) == 7 and validate_hex(pp['hcl'][1:])):
        print("hcl:" + str(pp))
        return False
    if not(pp['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]):
        print("ecl:" + str(pp))
        return False
    if not(len(pp['pid']) == 9 and RepresentsInt(pp['pid'])):
        print("pid:" + str(pp))
        return False
    return True


new_valid_ports = []
valid_count = 0

for port in valid_ports:
    if validate_port(port):
        new_valid_ports.append(port)
        valid_count += 1
        # print(port)

print(len(new_valid_ports))
print(valid_count)