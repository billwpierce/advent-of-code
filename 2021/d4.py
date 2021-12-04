f = open('d4.txt', 'r') # Insert the correct day
# Use one of these, depending on the day's challenges
# input = f.read().splitlines()  # Raw Reading
input = f.read().split("\n\n") # Groups Across Multiple Lines
# input = [int(x) for x in input] # Lines of integers
# input = [x.split() for x in input] # Multi-part input lines, seperated by spaces
# input = [[x for x in line] for line in input] # 2d array of the input
# input = [x.split("\n") for x in input]
moves = input[0].split(",")

input = [[x.split() for x in group.split("\n")]for group in input[1:]]

boards = input

# print(moves)

min_turn = 0
min_score = -1
min_board = -1
min_unmarked = -1

for board in boards:
    col_count = [0 for i in range(5)]
    row_count = [0 for i in range(5)]
    sm_unmarked = sum([sum([int(board[x][y]) for y in range(5)]) for x in range(5)])
    for turn in range(len(moves)):
        for row in range(5):
            for col in range(5):
                if board[row][col] == moves[turn]:
                    col_count[col] += 1
                    row_count[row] += 1
                    sm_unmarked -= int(board[row][col])
        if max(max(col_count), max(row_count)) >= 5:
            if turn > min_turn:
                min_turn = turn
                min_score = int(moves[turn]) * sm_unmarked
            break

print(min_score)