# line = input()

line = 'a aa abC aa ac abc bcd a'.lower().split(' ')

words = [word + ' ' + str(line.count(word)) for word in set(line)]

print('\n'.join(words))
