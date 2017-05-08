classes = dict()
for x in range(int(input())):
    res = input().split(' : ')
    if len(res) == 1:
        classes[res[0]] = [res[0]]
    else:
        classes[res[0]] = classes.get(res[0], []) + res[1].split(' ')

for k, v in classes.items():
    for k1, v1 in classes.items():
        if k in v1:
            v1 += v

for x in range(int(input())):
    res = input().split(' ')
    if res[0] in classes[res[1]]:
        print('Yes')
    else:
        print('No')
