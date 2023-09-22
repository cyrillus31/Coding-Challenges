amount_input = int(input())

direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# def walk(price, target):
#     depth = price - 1
#     max_steps = ((10 - depth*2) * 2) + ((10 - depth*2 - 2)  * 2)
#     start = (depth, depth)
#     for 

def hor_split(arr, dir, mirror_h: bool):
    if mirror_h:
        m = -1
    else: 
        m = 1
    if dir == "up":
        new_arr = arr[:(len(arr)//2)-1]
    if dir == "down":
        new_arr = arr[len(arr)//2:]

    return new_arr[::m]

def vert_split(arr, dir, mirror_v: bool):
    if mirror_v:
        m = -1
    else: 
        m = 1
    if dir == "left":
        new_arr = [row[:(len(row)//2):m] for row in arr[:]]
    if dir == "right":
        new_arr = [row[len(row)//2::m] for row in arr[:]]
    return new_arr[:]


def parse_upper_left(arr):
    counter = 0
    result = 0
    while counter < 5:
        to_parse = arr[counter][counter:]
        result += to_parse.count("X") * (counter + 1)
        counter += 1
    return result
        
        
        
    
    


for _ in range(amount_input):
    target = []
    for __ in range(10):
        target.append([symbol for symbol in input()])

    left_half = vert_split(target, "right", mirror_v=False)
    right_half = vert_split(target, "right", mirror_v=True)

    [print(line) for line in target]
    print("\n")
    

    upper_left = hor_split(left_half, 'up', False)
    upper_right = hor_split(right_half, "up", False)
    lower_left = hor_split(left_half, "down", True)
    lower_right = hor_split(right_half, "down", True)

    [print(line) for line in upper_right]
    print("\n")
    [print(line) for line in upper_left]
    print("\n")

    q = [upper_left, upper_right, lower_left, lower_right]


    result = [] 
    for quart in q:
        for line in quart:
            # print(line)
            pass
        print("\n")
        result.append(parse_upper_left(quart))

    print(result)

    break


    



    



    
















