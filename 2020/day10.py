from collections import defaultdict


def partA(voltages):
    jolts = 0
    seen = [0]
    ones = 0
    threes = 0
    while True:
        options = [(jolts+1), (jolts+2), (jolts+3)]

        selections = []
        for option in options:
            if option in voltages and option not in seen:
                selections.append(option)
        selected = min(selections)
        diff = selected - seen[-1]
        if diff == 1:
            ones += 1
        else:
            threes += 1
        seen.append(selected)
        jolts = selected
        if jolts == voltages[-1]:
            break
    return ones*(threes+1)


def partB(voltages):
    visited = [0] * (voltages[-1] + 1)
    # One way to get to zero
    visited[0] = 1
    for v in voltages:
        for i in range(1, 4):
            if visited[v - i]:
                visited[v] += visited[v - i]
    return visited[-1]


if __name__ == "__main__":
    voltages = [int(line.strip())
                for line in open('inputs/day10.txt').readlines()]
    voltages.sort()
    print(partA(voltages))
    print(partB(voltages))
