def disemvowel(string):
    return ''.join(list(filter(lambda x: x.lower() not in 'aeiou', string)))


def series_sum(n):
    res = sum([1 / (1 + 3 * (x - 1)) for x in range(1, n + 1)])
    return str('%.2f' % round(res, 2))
