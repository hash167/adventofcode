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
    # Memoization
    visited = defaultdict(int)
    # Number of times we visit a node
    visited[0] = 1
    for num in voltages:
        for i in range(1, 4):
            if num - i in visited:
                visited[num] += visited[num - i]
    return visited[max(voltages)]  


if __name__ == "__main__":
    voltages = [int(line.strip())
                for line in open('inputs/day10.txt').readlines()]
    voltages.sort()
    print(partA(voltages))
    print(partB(voltages))
