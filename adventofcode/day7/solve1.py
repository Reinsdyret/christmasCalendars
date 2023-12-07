class Hand:
    def __init__(self, hand, bet):
        self.hand = hand
        self.bet = bet

    def priority(self):
        hand_set = set(self.hand)

        if len(hand_set) == 1:
            return 6

        if len(hand_set) == 2:
            a, b = hand_set
            lenA, lenB = (self.hand.count(a), self.hand.count(b))

            if (lenA == 3 and lenB == 2) or (lenB == 3 and lenA == 2):
                return 4

            if (lenA == 4 and lenB == 1) or (lenB == 4 and lenA == 1):
                return 5

        if len(hand_set) == 3:
            lengths = [self.hand.count(i) for i in self.hand]

            return max(lengths)

        if len(hand_set) == 4:
            return 1

        return 0

    def card_priority(self, card):
        mapping = {
                '2':1,
                '3':2,
                '4':3,
                '5':4,
                '6':5,
                '7':6,
                '8':7,
                '9':8,
                'T':9,
                'J':10,
                'Q':11,
                'K':12,
                'A':13
                }

        return mapping[card]
        
    def __lt__(self, other):
        # If hand is less than full house / quads and the hands do not have the same amount of pairs
        if(len(set(self.hand)) > 2) and len(set(self.hand)) != len(set(other.hand)):
            return len(set(self.hand)) > len(set(other.hand))

        if self.priority() != other.priority():
            return self.priority() < other.priority()

        for i in range(len(self.hand)):
            if self.card_priority(self.hand[i]) != other.card_priority(other.hand[i]):
                return self.card_priority(self.hand[i]) < other.card_priority(other.hand[i])

        return False




    def __str__(self):
        return f"{self.hand} {self.bet}"

all_hands = []

with open('input.txt', 'r') as f:
    for line in f:
        hand, value = line.strip().split(' ')
        all_hands.append(Hand(hand,int(value)))

total_value_sum = 0
all_hands = sorted(all_hands)
for i in range(len(all_hands)):
    value = all_hands[i].bet
    total_value_sum += value * (i+1)

print(total_value_sum)

