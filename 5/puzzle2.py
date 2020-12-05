def parse(lines):
    data = []
    for line in lines:
        inst = line.strip()
        inst = inst.replace('B', '1')
        inst = inst.replace('F', '0')
        inst = inst.replace('R', '1')
        inst = inst.replace('L', '0')
        data.append(inst)
    return data

def solve(data):
    ids = getIds(data)
    missing = [x for x in range(ids[0], ids[-1] + 1) if x not in ids]
    print missing
    return 0

def getIds(data):
    idList = []
    for ticket in data:
        row = int(ticket[0:7],2)
        col = int(ticket[7:11],2)
        idList.append(int(bin((row << 3) + col), 2))
    idList.sort()
#    print(idList)
    return idList
