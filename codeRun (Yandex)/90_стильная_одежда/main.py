from sys import exit

top_amount = int(input())
tops = list(map(int, input().split()))

short_amount = int(input())
shorts = list(map(int, input().split()))


one = 0
two = 0

result = {
        "diff": None,
        "index": None,
        }

while one < top_amount and two < short_amount:
    top = tops[one]
    short = shorts[two]
    diff = abs(top - short)
    if diff == 0:
        print(tops[one], shorts[two])
        exit()

    if result["diff"]:
        if diff < result["diff"]:
            result["diff"] = diff
            result["index"] = (one, two)


    else:
        result["diff"] = diff
        result["index"] = (one, two)

    if min(top, short)  == short:
        if two < (short_amount - 1):
            two += 1
        elif one < (top_amount - 1):
            one += 1
    else:
        if one < (top_amount - 1):
            one += 1
        elif two < (short_amount - 1):
            two += 1

    if one == len(tops) - 1 and two == len(shorts) - 1:
        break

a, b = result["index"]
print(tops[a], shorts[b])
exit()



