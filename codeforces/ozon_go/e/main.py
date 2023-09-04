amount_of_friends, amount_total_cards = input().split()
amount_of_friends, amount_total_cards = int(amount_of_friends), int(amount_total_cards)

if amount_total_cards < amount_of_friends:
    print('-1')
    exit()


cards_of_friends = list(map(int, input().split()))
r = {card: [] for card in cards_of_friends}

sorted_friends = sorted(cards_of_friends, reverse=True)

for friend_card in sorted_friends:
    if friend_card >= amount_total_cards:
        print('-1')
        exit()
    r[friend_card].append(amount_total_cards) 
    amount_total_cards -= 1

result = []
for friend in cards_of_friends:
    result.append(str(r[friend].pop()))

print(' '.join(result))



















# ranges = {}
# for friend_card in cards_of_friends:
    # range = [friend_card, amount_total_cards]
    # if range not in ranges:
        # ranges[range] = 1
    # else:
        # ranges[range] += 1



