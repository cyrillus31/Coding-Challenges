a = int(input())

for a in range(a):
    amount_of_people = int(input())
    temp_range = [15, 30]
    fail_check = False
    for i in range(amount_of_people):
        sign, adjust_temp = input().split()
        adjust_temp = int(adjust_temp)
        if fail_check:
            print('-1')
            continue
        if sign[0] == '>':
            if adjust_temp > temp_range[1]:
                print('-1')
                fail_check = True
                continue
            if adjust_temp > temp_range[0]:
                temp_range[0] = adjust_temp
        if sign[0] == '<':
            if adjust_temp < temp_range[0]:
                print('-1')
                fail_check = True
                continue
            if adjust_temp < temp_range[1]:
                temp_range[1] = adjust_temp
        print(temp_range[0])
    print('\n')



    
