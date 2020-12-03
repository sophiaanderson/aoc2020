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
    return trueOccurances(int(range[0]),int(range[1]), letter, passw)


def trueOccurances(index1, index2, letter, passw):
        return ((passw[index1 - 1] == letter) ^ (passw[index2 - 1] == letter))
