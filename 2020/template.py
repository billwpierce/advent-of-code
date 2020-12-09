f = open('day_input.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
inp = f.read().splitlines()  # Raw Reading
# inp = f.read().split("\n\n") # Groups Across Multiple Lines
# inp = [int(x) for x in inp] # Lines of integers
# inp = [x.split() for x in inp] # Multi-part input lines, seperated by spaces