
colorMinPowerSum = 0

def miniMumColors(line):
    game, games = line.split(':')
    _, gameId = game.split(' ')
    games = games.split(';')

    mins = {
            'red':0,
            'green':0,
            'blue':0
            }
    
    for game in games:
        for draw in game.split(','):
            number, color = draw.strip().split(' ')
            if int(number) > mins[color]:
                mins[color] = int(number)
    return mins

with open('input.txt', 'r') as f:
    for line in f:
        mins = miniMumColors(line)
        colorMinPowerSum += mins['red'] * mins['green'] * mins['blue']

print(colorMinPowerSum)

