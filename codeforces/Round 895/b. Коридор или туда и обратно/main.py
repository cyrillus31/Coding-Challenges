amount_of_sets = int(input())

# compose a set
for _ in range(amount_of_sets):
    amount_traps = int(input())

    # create a hash table of traps
    traps = {}
    for i in range(amount_traps):
        placement, time = list(map(int, input().split()))
        if placement in traps:
            traps[placement].append(time - 1)
        else:
            traps[placement] = [time - 1]
    traps = dict(sorted(traps.items()))
    # solving a set
    print(traps)

    k = None
    for trap in traps:
        time_in_one_direction = min(traps[trap]) // 2
        max = trap + time_in_one_direction
        if k:
            if max < k:
                k = max
        else:
            k = max

    print(k)
