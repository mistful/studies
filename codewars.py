def disemvowel(string):
    return ''.join(list(filter(lambda x: x.lower() not in 'aeiou', string)))


def series_sum(n):
    res = sum([1 / (1 + 3 * (x - 1)) for x in range(1, n + 1)])
    return str('%.2f' % round(res, 2))


def alphabet_position(text):
    res = [str(ord(x.lower()) - 96) for x in text if 'a' <= x.lower() <= 'z']
    return ' '.join(res)


def longest(s1, s2):
    return ''.join(sorted(list(set(s1 + s2))))


class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack


def declare_winner(fighter1, fighter2, first_attacker):
    winner = ''

    attacker = fighter1 if first_attacker == fighter1.name else fighter2
    defender = fighter1 if attacker == fighter2 else fighter2
    tmp = None

    while fighter1.health > 0 and fighter2.health > 0:
        defender.health -= attacker.damage_per_attack
        print(attacker.name + ' attacks ' + defender.name + ' for ' + str(
            attacker.damage_per_attack) + 'HP. ' + defender.name + ' has ' + str(defender.health) + ' HP.')

        tmp = attacker
        attacker = defender
        defender = tmp

    return fighter1.name if fighter1.health > 0 else fighter2.name