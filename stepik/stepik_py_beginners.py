import csv

with open('dataset_3363_4.txt', 'r') as inputFile:
    reader = csv.reader(inputFile, delimiter=';')

    students = [line for line in reader]
    totalPoints = [[int(point) for point in points[1:]] for points in students]

    averages = '\n'.join([str(sum(point) / 3) for point in totalPoints])

    print(averages)

    totals = [[sum(point) for point in points] for points in totalPoints]

    print(totals)

