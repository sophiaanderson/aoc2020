import numpy as np

def parse(lines):
    data = []
    for line in lines:
        line = line.strip()
        data.append(list(line))
    return data

def solve(data):
    treeCount = 0
    col = 0
    rowlen = len(data[0])

    for row in data:
        space = row[col]
        if (space == '#'):
             treeCount = treeCount + 1
        col = (col + 3) % rowlen
    print(treeCount)
    return 0
