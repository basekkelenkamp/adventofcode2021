import csv
from pprint import pprint

list_data = []
boards = {}
new_board = {}
b_row_count = 0
with open('4.csv', newline='') as inputfile:
    for index, row in enumerate(csv.reader(inputfile)):
        # pprint(row)
        if len(row) > 25:
            list_draw_numbers = row
            continue

        if len(row) == 0:
            list_data.append(new_board)
            new_board = {}
            b_row_count = 0

        if len(row) == 1:
            row_stripped = row[0].replace("  ", " ").replace(" ", ",")
            if row_stripped[0] == ",":
                row_stripped = [row_stripped[1:]]
                print(row_stripped)
                new_board[str(index)] = row_stripped
            b_row_count = 1
            # for


        # list_data.append(row[0])
breakpoint()
print(list_data)
