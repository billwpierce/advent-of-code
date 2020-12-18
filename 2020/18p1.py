f = open('in18t.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

def reverse_list(lst):
    if lst == []:
        return []
    val = lst.pop()
    if val == "(":
        val = ")"
    elif val == ")":
        val = "("
    return [val] + reverse_list(lst)

input = [reverse_list([c for c in line.replace(" ", "")]) for line in input]
print(input[0])

def RepresentsInt(s): # https://stackoverflow.com/questions/1265665/how-can-i-check-if-a-string-represents-an-int-without-using-try-except
    try: 
        int(s)
        return True
    except ValueError:
        return False

class Pair():
    def __init__(self, first, rest=None):
        self.first = first
        self.rest = rest
    
    def __repr__(self):
        return "Pair(" + repr(self.first) + ", " + repr(self.rest) + ")"

def read_list(tokens):
    if len(tokens) == 0:
        return None
    val = tokens.pop(0)
    if RepresentsInt(val):
        return Pair(int(val), read_list(tokens))
    elif val in ["+", "*"]:
        return Pair(val, read_list(tokens))
    elif val == "(":
        return Pair(read_list(tokens), read_list(tokens))
    elif val == ")":
        return None
    else:
        print(val, "weird value")

# def apply()

def eval(p):
    print(p)
    if type(p) == int:
        return p
    elif p.rest == None:
        return eval(p.first)
    elif p.rest.first == "+":
        return eval(p.first) + eval(p.rest.rest)
    elif p.rest.first == "*":
        return eval(p.first) * eval(p.rest.rest)

sm = 0
for line in input:
    sm += eval(read_list(line))

print(sm)