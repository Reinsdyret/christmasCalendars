class Hand:
    def __init__(self, hand, bet):
        self.hand = hand
        self.bet = bet

    def priority(self):
        hand_set = set(self.hand)

        if 'J' in hand_set:
            return self.jack_corrected()

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
                'J':0,
                '2':1,
                '3':2,
                '4':3,
                '5':4,
                '6':5,
                '7':6,
                '8':7,
                '9':8,
                'T':9,
                'Q':10,
                'K':11,
                'A':12
                }

        return mapping[card]
        
    def __lt__(self, other):

        if self.priority() != other.priority():
            return self.priority() < other.priority()

        for i in range(len(self.hand)):
            if self.card_priority(self.hand[i]) != other.card_priority(other.hand[i]):
                return self.card_priority(self.hand[i]) < other.card_priority(other.hand[i])

        return False


    def jack_corrected(self):
        count_j = self.hand.count('J')

        if count_j == 5:
            # You have all Jokers and should keep all Aces
            copy_hand = self.hand
            self.hand = "AAAAA"
            priority  = self.priority()
            self.hand = copy_hand
            return priority

        # Remove all jacks
        copy_hand = self.hand

        while 'J' in self.hand:
            self.hand = self.hand.replace('J', '')

        # Get the most frequent card 
        best_card = max([(u, self.hand.count(u)) for u in set(self.hand)], key = lambda x: x[1])

        # Add the number of jokers as this best hand to the hand and get priority
        self.hand += best_card[0] * count_j

        priority = self.priority()

        # Change back into original hand and return
        self.hand = copy_hand
        return priority


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
print(list(map(str,all_hands)))

