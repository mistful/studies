import itertools


def primes():
    a = 1
    yield 2

    while True:
        a += 2



print(list(itertools.takewhile(lambda x: x <= 31, primes())))
