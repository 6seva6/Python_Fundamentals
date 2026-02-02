input_cards = input().split()
shuffle_count = int(input())

for _ in range(shuffle_count):
    current_cards_combination = []
    half_cards = len(input_cards) // 2
    left_side = input_cards[:half_cards]
    right_side = input_cards[half_cards:]

    for i in range(half_cards):
        current_cards_combination.append(left_side[i])
        current_cards_combination.append(right_side[i])
    input_cards = current_cards_combination

print(input_cards)
