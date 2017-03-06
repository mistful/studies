# n = int(input())
# for i in range(0, n):
#     games.add(input().split(';'))

with open('games.txt') as g:
    games = g.readlines()

games = [game.strip() for game in games]
teams = {}

for game in games:
    res = game.split(';')
    teams[res[0]] = teams.get(res[0], {})



print(teams)