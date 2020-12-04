import sys


def partA(inputs: list) -> int:
    ret = 0
    for item in inputs:
        a_range = [int(s) for s in item[0].split("-")]
        alpha = item[1][:-1]
        count = list(item[2]).count(alpha)
        if a_range[0] <= count <= a_range[1]:
            ret += 1
    return ret


def partB(inputs: list) -> int:
    ret = 0
    for item in inputs:
        a_range = [int(s) for s in item[0].split("-")]
        alpha = item[1][:-1]
        if (list(item[2])[a_range[0] - 1] == alpha and list(item[2])[a_range[1] - 1] != alpha) or \
           (list(item[2])[a_range[0] - 1] != alpha and list(item[2])[a_range[1] - 1] == alpha):
            ret += 1
    return ret


if __name__ == "__main__":
    inputs = []
    with open('inputs/day2.txt') as f:
        for line in f:
            inputs.append(line.strip().split(" "))
    if sys.argv[1] == 'A':
        print(partA(inputs))
    else:
        print(partB(inputs))
