import sys


def partB(inputs: list) -> int:
    return 0


if __name__ == "__main__":
    index = 3
    trees = 0
    add = False
    with open('inputs/day3.txt') as f:
        for line in f:
            if not add:
                add = not add
                continue
            row = list(line.strip())
            index = index % len(row)
            if row[index] == '#':
                trees += 1
            index += 3
    if sys.argv[1] == 'A':
        print(trees)
    else:
        pass
