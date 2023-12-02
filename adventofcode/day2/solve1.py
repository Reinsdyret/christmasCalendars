
blueLimit = 14
greenLimit = 13
redLimit = 12

limits = {
        'blue':14,
        'green':13,
        'red':12
        }
gameIdSum = 0

def validGame(line):
    game, games = line.split(':')
    _, gameId = game.split(' ')
    games = games.split(';')
    
    for game in games:
        for draw in game.split(','):
            number, color = draw.strip().split(' ')
            if int(number) > limits[color]:
                return 0

    return int(gameId)

with open('input.txt', 'r') as f:
    for line in f:
        gameIdSum += validGame(line)

print(gameIdSum)

