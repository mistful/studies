a, b = (int(input()) for x in range(2))

firstDiv = a if 0 == a % 3 else (a // 3 + 1) * 3
dividing = list(filter(lambda x: 0 == x % 3, range(a, b + 1)))
print(sum(dividing) / len(dividing))