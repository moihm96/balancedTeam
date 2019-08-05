import operator
ids = ["Alice", "Bob", "Coral", "David"]
scores = [4.5, 6.1, 5.2, 4.7]

ids1 = ["Felipe", "Joao", "Thiago", "Leao", "Veronica", "Luisa", "Marta", "Cynthia"]
scores1 = [7.1, 7.9, 8, 7.5, 6.5, 5.7, 5.2, 6.9]


def players_score(self, scores):
    players = {}
    for i in range(0, len(self)):
        players.update({self[i]: scores[i]})
    return players


def player_split(self, score):
    players = players_score(self, score)
    result = sorted(players.items(), key=operator.itemgetter(1), reverse = True)
    team1 = []
    team2 = []
    score1 = []
    score2 = []
    for k, v in result:
        if suma(score1) > suma(score2):
            team2.append(k)
            score2.append(v)
        else:
            team1.append(k)
            score1.append(v)
    return team1, team2


def suma(self):
    b = 0
    for i in self:
        b = b + i
    return b


print(player_split(ids, scores))
print(player_split(ids1, scores1))
