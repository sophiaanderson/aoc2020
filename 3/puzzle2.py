

def parse(lines):
    data = []
    for line in lines:
        line = line.strip()
        data.append(list(line))
    return data

def solve(data):
    trees = (findTrees(1, 1, data) * findTrees(3, 1, data) * findTrees(5, 1, data)
            * findTrees(7, 1, data) * findTrees(1, 2, data))
    print(trees)
    return 0


def findTrees(right, down, data):
    r = 0
    col = 0
    treeCount = 0
    rowlen = len(data[0])
    while r < len(data):
        row = data[r]
        space = row[col]
        if (space == '#'):
            treeCount = treeCount + 1
        col = (col + right) % rowlen
        r = r + down
    print(treeCount)
    return treeCount
