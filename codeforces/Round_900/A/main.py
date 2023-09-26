from sys import exit

amount = int(input())

def check_contains(l1, l2):
    result = 1
    for e in l1:
       result *= (e in range(l2[0], l2[-1] + 1))
    return bool(result)
        

for _ in range(amount):
    d = {}
    n, k = list(map(int, input().split()))
    arr_gen = (map(int, input().split()))

    for i in arr_gen:
        if i not in d:
            d[i] = {"l": 1, "pos": [i]}
        else:
            d[i]["l"] += 1
            d[i]["pos"].append(i)

    # print(d)

    if k not in d:
        print('NO')
        continue

    frequency = d[k]["l"]
    result = 1
    for number in filter(lambda x: d[x]["l"] >= frequency, d):
        positions = d[number]["pos"]
        target_positions = d[k]["pos"]
        result *= check_contains(positions, target_positions)
    if result is True:
        print("NO")
    else:
        print("YES")



