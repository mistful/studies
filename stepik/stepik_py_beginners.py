import collections

with open('dataset_3380_5.txt') as data:
    classes = [line.strip().split('\t') for line in data.readlines()]

result = {k: [] for k in range(1, 12)}

for cl in classes:
    result[int(cl[0])].append(int(cl[2]))

result = '\n'.join([str(k) + ' ' + val for k, val in {k: str(sum(val) / len(val)) if len(val) else '-' for k, val in result.items()}.items()])

print(result)
