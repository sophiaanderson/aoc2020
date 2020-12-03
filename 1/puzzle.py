def parse(lines):
    inp = []
    for line in lines:
        inp.append(int(line))
    return inp

def solve(data):
    for point in data:
        diff = 2020 - point
        for i in data:
            if (i == diff):
                print (point * diff)
                return (point * diff)
    return -1
