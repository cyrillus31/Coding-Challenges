amount = int(input())
for i in range(amount):
    amount_of_prices = input()
    prices = [int(price) for price in input().split()]

    result = {}
    sum = 0
    for price in prices:
        if price not in result:
            result[price] = 1
        else:
            result[price] += 1

    for price in result:
        if result[price] == 1:
            sum += price
            continue
        quotient, remainder = divmod(result[price], 3)
        sum += quotient * 2 * price + remainder * price
    print(sum)
