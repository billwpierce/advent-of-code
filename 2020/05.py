original_input = open('in05.txt', 'r') 
all_lines = original_input.readlines()

def get_row(row_str):
    min_r, max_r = 0, 127
    for c in row_str:
        if c == "F":
            max_r = min_r + ((max_r - min_r) + 1)/2 - 1
        elif c == "B":
            min_r = min_r + ((max_r - min_r) + 1)/2
    if min_r == max_r:
        return min_r
    else:
        return "reeee"

def get_col(col_str):
    min_c, max_c = 0, 7
    for c in col_str:
        if c == "L":
            max_c = min_c + ((max_c - min_c) + 1)/2 - 1
        elif c == "R":
            min_c = min_c + ((max_c - min_c) + 1)/2
    if min_c == max_c:
        return min_c
    else:
        return "reeee"

def get_seat(pos_str):
    return get_row(pos_str[:7]), get_col(pos_str[7:])

def get_seatID(row, col):
    return int(row) * 8 + int(col)

seat_ids = []

for line in all_lines:
    seat_ids.append(get_seatID(*get_seat(line)))

mx = max(seat_ids)

possible_seats = list(range(mx+1))

for st in seat_ids:
    possible_seats.remove(st)

print(possible_seats)