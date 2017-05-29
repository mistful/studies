class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.funcs = list(funcs)
        self.iterable = iterable
        self.judge = judge

    def __iter__(self):
        for element in self.iterable:
            neg = pos = 0

            for func in self.funcs:
                if func(element):
                    pos += 1
                else:
                    neg += 1

            if self.judge(pos, neg):
                yield element


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
