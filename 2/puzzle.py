def parse(lines):
    input = []
    for line in lines:
        input.append(line)
    return input


def solve(data):
    countValid = 0
    for line in data:
        params = line.split(' ')
        if validpassword(params):
            countValid = countValid + 1
    print(countValid)

def validpassword(params):
    range = params[0].split('-')
    letter = params[1].replace(':', '')
    passw = params[2]
    return numOccurances(int(range[0]),int(range[1]), letter, passw)


def numOccurances(min, max, letter, passw):
    count = 0
    for c in passw:
        if (c == letter):
            count = count + 1
    if (count >= min) and (count <= max):
        return True
