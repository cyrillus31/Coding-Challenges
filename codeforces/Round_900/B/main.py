from collections import deque 

amount = int(input())

for _ in range(amount):
    result = deque()
    stack = deque()
    n = int(input())
    for i in range(1, n+1):
        if len(stack) < 2:
            stack.append(i)
            continue
        a2 = stack.pop()
        a1 = stack.pop()
        while (a1 + a2) % 3 == 0:
            a2 += 1
            a3 = a2 + 1
        while (3 * a3) % (a1 + a2) == 0 or a2 == a3:
            a3 += 1
        stack.extend([a1, a2, a3])
    print(" ".join(map(str, stack)))

    



