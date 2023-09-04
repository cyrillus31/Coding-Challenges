amount_of_tasks = int(input())


def check_if_not_dot(row_number, symbol_number):
    for view in views[1:]:
        symbol = view[row_number][symbol_number]
        if symbol != ".":
            return symbol
    return None


for a in range(amount_of_tasks):
    amount, rows, columns = input().split()
    amount, rows, columns = int(amount), int(rows), int(columns)
    views = [[] for empty in range(amount)]

    for i_views in range(amount):
        for i in range(rows):
            row = [symbol for symbol in input()]
            views[i_views].append(row)
        if i_views != amount - 1:
            skip_empty_row = input()

    # for view in views:
    # for row in view:
    # print("".join(row))

    result_view = []
    for i in range(rows):
        row_number = i
        symbol_number = 0
        result_row = views[0][row_number]
        for symbol in result_row:
            if symbol == ".":
                replace_symbol = check_if_not_dot(row_number, symbol_number)
                if replace_symbol:
                    result_row[symbol_number] = replace_symbol
            symbol_number += 1
        result_view.append(result_row)

    for row in result_view:
        print("".join(row))
    print("")
