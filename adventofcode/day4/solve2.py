number_of_cards = {}
winning_numbers = {}

with open('input.txt', 'r') as f:
    for line in f:
        cardId, card = line.split(':')
        cardId = cardId.strip().split(" ")[-1]
        winningNumbers, numbers = card.split('|')
        winningNumbers = set(winningNumbers.strip().split(' '))
        numbers = set(numbers.strip().split(' '))

        while '' in numbers:
            numbers.remove('')

        while '' in winningNumbers:
            winningNumbers.remove('')

        number_of_cards[int(cardId)] = 1

        winning_numbers[int(cardId)] = len(winningNumbers.intersection(numbers))


for cardId in range(1, len(number_of_cards) + 1):
    for newCardId in range(cardId + 1, min(cardId + 1 + winning_numbers[cardId], len(number_of_cards) + 1)):
        number_of_cards[newCardId] += number_of_cards[cardId] 

print(sum([number_of_cards[card] for card in number_of_cards]))

