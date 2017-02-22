def disemvowel(string):
    return ''.join(list(filter(lambda x: x.lower() not in 'aeiou', string)))


def longest_consec(strarr, k):
    n = len(strarr)

    if k > n or n == 0 or k <= 0:
        return ""

    

