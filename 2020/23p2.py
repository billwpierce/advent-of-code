f = open('in23.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
input = f.read().splitlines()  # Raw Reading
# input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]

class LinkedList:
    def __init__(self, first=None, rest=None):
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest == None:
            return "LinkedList(" + repr(self.first) + ", " + repr(self.rest) + ")"
        elif self.rest.rest == None:
            return "LinkedList(" + repr(self.first) + ", " + "LinkedList(" + repr(self.rest.first) + ", " + repr(self.rest.rest) + ")" + ")" + ")"
        elif self.rest.rest.rest == None:
            return "LinkedList(" + repr(self.first) + ", " + "LinkedList(" + repr(self.rest.first) + ", " + "LinkedList(" + repr(self.rest.rest.first) + ", " + repr(self.rest.rest.rest) + ")" + ")" + ")" + ")"
        else:
            return "LinkedList(" + repr(self.first) + ", " + "LinkedList(" + repr(self.rest.first) + ", " + "LinkedList(" + repr(self.rest.rest.first) + ", " + "LinkedList(" + repr(self.rest.rest.rest.first) + ", " + "LinkedList(...)" + ")" + ")" + ")" + ")"

val_location = {}        
cups = list(range(1, 10000001))
lst = LinkedList(6, LinkedList(4, LinkedList(3, LinkedList(7, LinkedList(1, LinkedList(9, LinkedList(2, LinkedList(5, LinkedList(8)))))))))
# lst = LinkedList(3, LinkedList(8, LinkedList(9, LinkedList(1, LinkedList(2, LinkedList(5, LinkedList(4, LinkedList(6, LinkedList(7)))))))))
i = 10
_node = lst.rest.rest.rest.rest.rest.rest.rest.rest
print(_node)
while i <= 1000000:
    _node.rest = LinkedList(i, None)
    _node = _node.rest
    i+=1

i = 0
temp = lst
while temp != None:
    val_location[temp.first] = temp
    temp = temp.rest
    i += 1
_node.rest = lst
curr_cup = lst
for i in range(10000000):
    if i % 100000 == 0:
        print(i)
    temp = [curr_cup.rest.first, curr_cup.rest.rest.first, curr_cup.rest.rest.rest.first]
    curr_cup.rest = curr_cup.rest.rest.rest.rest
    label = curr_cup.first - 1
    if label < 1:
        label = max(val_location.keys())
    while label in temp:
        label -= 1
        if label < 1:
            label = max(val_location.keys())
    insert_cup = val_location[label]
    insert_cup.rest = LinkedList(temp[0], LinkedList(temp[1], LinkedList(temp[2], insert_cup.rest)))
    icr = insert_cup.rest
    for lbl in temp:
        val_location[lbl] = icr
        icr = icr.rest
    curr_cup = curr_cup.rest
# print(val_location)

print(val_location[1])
