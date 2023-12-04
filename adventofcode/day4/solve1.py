
winnings = 0

with open('input.txt', 'r') as f:
    for line in f:
        cardId, card = line.split(':')
        winningNumbers, numbers = card.split('|')
        winningNumbers = set(winningNumbers.strip().split(' '))
        numbers = set(numbers.strip().split(' '))

        while '' in numbers:
            numbers.remove('')

        amountOfWinningNumbers = len(winningNumbers.intersection(numbers))


        if amountOfWinningNumbers > 0:
            winnings += 2 ** (amountOfWinningNumbers - 1)

print(winnings)
