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
    max = 0
    for ticket in data:
        row = int(ticket[0:7],2)
        col = int(ticket[7:11],2)
        id = (row << 3) + col
        if (max < id): max = id
    print(max)
    return 0
