with open("input4.txt", "r") as file:
    board = [[s for s in line] for line in file]

counter = 0

def is_out_of_bound(x, y):
    if x < 0 or x >= 8 or y < 0 or y >= 8:
        return True 
    return False 

def is_occupied(x, y):
    if board[x][y] == "*":
        return True
    return False

directions = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1)
        ]

for x in range(8):
    for y in range(8):
        variations = 0
        if is_occupied(x, y):
            continue
        for direction in directions:
            dx, dy = direction
            new_x = x + dx
            new_y = y + dy
            if not is_out_of_bound(new_x, new_y):
                if not is_occupied(new_x, new_y):
                    variations += 1
        if variations == 3:
            counter += 1
        elif variations == 4:
            counter += 4

print(counter)






