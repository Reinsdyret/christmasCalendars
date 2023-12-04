cardDict = {}
cardCount = 0

with open('testInput.txt', 'r') as f:
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

        cardDict[int(cardId)] = (1, (winningNumbers, numbers))


def insertNewCopies(cardId, cardDict):
    cardCount, (winningNumbers, numbers) = cardDict[cardId]

    winCount = len(winningNumbers.intersection(numbers)) * cardCount

    print(winCount)

    for i in range(cardId + 1, min(winCount + 1, len(cardDict))):
        count, const = cardDict[i]
        count += 1
        cardDict[i] = (count, const)

    return cardDict


cardId = 1

while cardId < len(cardDict):
    insertNewCopies(cardId, cardDict)
    cardId += 1


for k,v in cardDict.items():
    print(f"{k} : {v}")

sum_of_cards = 0

for cardId in cardDict:
    count, rest = cardDict[cardId]

    sum_of_cards += count

print(sum_of_cards)
