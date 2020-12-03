import sys


def partA(inputs: list) -> int:
    seen = []
    for i in range(len(inputs)):
        rem = 2020 - inputs[i]
        if inputs[i] in seen:
            return rem * inputs[i]
        seen.append(rem)
    return 0


def partB(inputs: list) -> int:
    input_length = len(inputs)
    seen = []
    for i in range(input_length):
        for j in range(input_length):
            if i == j:
                continue
            partial_sum = inputs[i] + inputs[j]
            if partial_sum > 2020:
                continue
            else:
                seen.append(partial_sum)
            for k in range(input_length):
                if (2020 - inputs[k]) in seen and (k != j or k != i):
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
