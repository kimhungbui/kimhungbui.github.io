from collections import Counter

# Step 1: Value mapping
CARD_VALUES = {'2': 2, '3': 3, '4': 4, '5': 5,
               '6': 6, '7': 7, '8': 8, '9': 9,
               'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

# Step 2: Evaluate hand
def hand_rank(hand):
    values = sorted([CARD_VALUES[c[0]] for c in hand], reverse=True)
    suits = [c[1] for c in hand]
    counts = Counter(values)
    count_vals = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
    ordered_values = [val for val, cnt in count_vals]

    is_flush = len(set(suits)) == 1
    is_straight = values == list(range(values[0], values[0]-5, -1))

    if is_straight and is_flush:
        return (8, values)
    elif count_vals[0][1] == 4:
        return (7, ordered_values)
    elif count_vals[0][1] == 3 and count_vals[1][1] == 2:
        return (6, ordered_values)
    elif is_flush:
        return (5, values)
    elif is_straight:
        return (4, values)
    elif count_vals[0][1] == 3:
        return (3, ordered_values)
    elif count_vals[0][1] == 2 and count_vals[1][1] == 2:
        return (2, ordered_values)
    elif count_vals[0][1] == 2:
        return (1, ordered_values)
    else:
        return (0, values)

# Step 3: Compare two hands
def player1_wins(hand1, hand2):
    return hand_rank(hand1) > hand_rank(hand2)

# Step 4: Process file
def count_player1_wins(filename='poker.txt'):
    count = 0
    with open(filename) as f:
        for line in f:
            cards = line.strip().split()
            hand1 = cards[:5]
            hand2 = cards[5:]
            if player1_wins(hand1, hand2):
                count += 1
    return count

# Step 5: Output result
print(count_player1_wins())