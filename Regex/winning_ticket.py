import re

list_tickets = input().split(', ')

for ticket in list_tickets:
    ticket = ticket.strip()
    if len(ticket) != 20:
        print(f'invalid ticket')
    else:
        left_side = ticket[:10]
        right_side = ticket[10:20]

        pattern = r'[@,#,$,^]{6,}'

        left_match = re.search(pattern, left_side)
        right_match = re.search(pattern, right_side)

        if not left_match or not right_match:
            print(f'ticket "{ticket}" - no match')
            continue

        left_match = left_match.group()
        right_match = right_match.group()
        uninterrupted_match_length = 0

        if len(left_match) > len(right_match):
            uninterrupted_match_length = len(right_match)
        else:
            uninterrupted_match_length = len(left_match)
        match_symbol = left_match[0]

        if 6 <= uninterrupted_match_length < 10:
            print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}')

        else:
            print(f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!')