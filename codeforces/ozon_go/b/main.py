s = input()
amount_of_stickers = int(input())

for i in range(amount_of_stickers):
    first, last, sticker = input().split()
    first, last = int(first) - 1, int(last) - 1
    s = s[:first] + sticker + s[last+1:]

print(s)
