def show_menu(menu_list):
    index = 0
    print("\n")
    for element in menu_list:
        print(f"{index}. {element}")
        index += 1
    print("\n")

def initialize_theater(rows, columns):
    theater = []
    for i in range(rows):
        new_row = []
        for i in range(columns):
            new_row.append("0")

        theater.append(new_row)

    return theater

def show_theater(layout):
    index = 65
    index_columns = 1
    columns_nbr = "/  "
    l_row = layout[0]

    for i in range(len(l_row)):
        columns_nbr += f"{index_columns}  "
        index_columns += 1
    print(columns_nbr)

    for row in layout:
        to_display = f"{chr(index)}  "
        for seat in row:
            to_display += seat + "  "
        print(to_display)
        index += 1

def check_availability(row_seat, seat_nbr, theater):
    if theater[ord(row_seat) - 65][seat_nbr - 1] == "0":
        return True
    
def count_seats(layout):
    free = 0
    taken = 0

    for row in layout:
        for seat in row:
            if seat == "0":
                free += 1
            else:
                taken += 1
    
    return (free, taken)