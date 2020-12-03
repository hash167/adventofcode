import sys


def partA(inputs: list) -> int:
    l = len(inputs)
    for i in range(l):
        for j in range(l):
            if i == j:
                continue
            if (inputs[i]+inputs[j]) == 2020:
                return inputs[i]*inputs[j]
    return 0


def partB(inputs: list) -> int:
    l = len(inputs)
    for i in range(l):
        for j in range(l):
            for k in range(l):
                if i == j or j == k or i == k:
                    continue
                if (inputs[i] + inputs[j] + inputs[k]) == 2020:
                    return inputs[i] * inputs[j] * inputs[k]
    return 0


if __name__ == "__main__":
    inputs = []
    with open('inputs/day1.txt') as f:
        for line in f:
            num = int(line)
            # eliminate inputs greater than 2020
            if num < 2020:
                inputs.append(num)
    if sys.argv[1] == 'A':
        print(partA(inputs))
    else:
        print(partB(inputs))
