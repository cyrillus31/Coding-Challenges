from sys import exit

amount = int(input())

for _ in range(amount):
    arr = input()
    if arr[0] == "a":
        if (arr[1:] == "bc") or (arr[1:] == "cb"):
            print("YES")
            continue
        else:
            print("NO")
            continue
    if arr[0] == "b":
        if (arr[1:] == "ac"):
            print("YES")
            continue
        else:
            print("NO")
            continue

    if arr[0] == "c":
        if arr[1:] == "ba":
            print("YES")
            continue
        else:
            print("NO")
            continue

