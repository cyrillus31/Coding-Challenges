amount = int(input())
l = []
for i in range(amount):
    l.append(list(map(int, input().split())))

for case in l:
    bucket1, bucket2, cup = case
    diff = abs(bucket1 - bucket2)
    amount, leftover = divmod(diff, 2*cup)
    if leftover != 0:
        amount += 1
    print(amount)
