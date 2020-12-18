f = open('in18.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading

input = [[c for c in line.replace(" ", "")] for line in input]

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

class Tree:
    """A tree."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches
    
    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

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

def convert_pair_to_list(p):
    if type(p) != Pair:
        return p
    elif p.rest == None:
        return [convert_pair_to_list(p.first)]
    else:
        return [convert_pair_to_list(p.first)] + convert_pair_to_list(p.rest)

def convert_list_to_pair(l):
    if type(l) != list:
        return l
    if len(l) == 0:
        return None
    else:
        return Pair(convert_list_to_pair(l[0]), convert_list_to_pair(l[1:]))

def pt(l): # Takes list, return trees
    nl = []
    for item in l:
        if type(item) == list:
            nl.append(pt(item))
        else:
            nl.append(item)
    mul_splits = []
    saved_index = 0
    if "*" in nl:
        for i in range(len(nl)):
            if nl[i] == "*":
                mul_splits.append(nl[saved_index:i])
                saved_index = i + 1
    mul_splits.append(nl[saved_index:])
    ns = []
    for split in mul_splits:
        tsplit = [split[len(split)-2*i-1] for i in range((len(split)+1)//2)]
        t = Tree("+")
        v = t
        for j in range(len(tsplit)-1):
            if type(tsplit[j]) == Tree:
                v.branches.append(tsplit[j])
            else:
                v.branches.append(Tree(tsplit[j]))
            v.branches.append(Tree("+"))
            v = v.branches[1]
        tmp = tsplit[len(tsplit)-1]
        if type(tmp) == int:
            v.label = tmp
        else:
            v.label, v.branches = tmp.label, tmp.branches
        ns.append(t)
    ns.reverse()
    if len(ns) > 1:
        t = Tree("*")
        v = t
        for j in range(len(ns)-1):
            if type(ns[j]) == Tree:
                v.branches.append(ns[j])
            else:
                v.branches.append(Tree(ns[j]))
            v.branches.append(Tree("*"))
            v = v.branches[1]
        tmp = ns[len(ns)-1]
        if type(tmp) == int:
            v.label = tmp
        else:
            v.label, v.branches = tmp.label, tmp.branches
        return t
    else:
        return ns[0]
    
def eval_from_tree(t):
    if t.is_leaf():
        return t.label
    if len(t.branches) != 2:
        raise Exception("What")
    if t.label == "*":
        t0 = eval_from_tree(t.branches[0])
        t1 = eval_from_tree(t.branches[1])
        return t0 * t1
    if t.label == "+":
        t0 = eval_from_tree(t.branches[0])
        t1 = eval_from_tree(t.branches[1])
        return t0 + t1

sm = 0
for line in input:
    sm += eval_from_tree(pt(convert_pair_to_list(read_list(line))))

print(sm)