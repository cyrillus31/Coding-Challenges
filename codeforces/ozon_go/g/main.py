suits = ('S', 'C', 'D', 'H')
values = ("2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A")

value_dict = {values[i]: i+2 for i in range(0, 13)}

deck = []
for suit in suits:
    for value in values:
        card = value+suit
        deck.append(card)

amount_players = int(input())
hands = []
for i in range(amount_players):
    hand = input().split()
    card1, card2 = hand
    deck.remove(card1)
    deck.remove(card2)
    hands.append(hand)

# myhand = hands.pop(0)

def is_set(hand, table):
    card1, card2 = hand
    if card1[0] == card2[0] == table[0]:
        return 100 
    return 0 

def is_pair(hand, table):
    card1, card2 = hand
    values = [card1[0], card2[0], table[0]]
    if len(set(values)) == 2:
        return 50
    return 0 

def highest_value(hand, table) -> int:
    card1, card2 = hand
    high = max(list(map(lambda string: value_dict[string], [card1[0], card2[0], table[0]])))
    return high

scores = []    
best_cards = []

d = {}
for table in deck:
    for hand in hands:
        score = is_set(hand, table) + is_pair(hand, table) + highest_value(hand, table) 
        scores.append(score)
    print(table, scores)
    if max(scores) == scores[0]:
        best_cards.append(table)
    scores = []
        
l = len(best_cards)
print(l)
for card in best_cards:
    print(card)







