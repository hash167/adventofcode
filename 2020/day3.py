import sys


if __name__ == "__main__":
    slopes = [(1, 2), (7, 1), (1, 1), (5, 1), (3, 1)]
    index_tracker = [1, 7, 1, 5, 3]
    skip_tracker = [2, 1, 1, 1, 1]
    trees = [0] * 5
    with open('inputs/day3.txt') as f:
        lines = 0
        for line in f:
            for i in range(len(slopes)):
                base_index = slopes[i][0]
                base_skip = slopes[i][1]
                if skip_tracker[i]:
                    skip_tracker[i] = skip_tracker[i] - 1
                    continue
                row = list(line.strip())
                if row[index_tracker[i] % len(row)] == '#':
                    trees[i] += 1
                index_tracker[i] += base_index
                if base_skip == 2:
                    skip_tracker[i] += 1
            lines += 1
    if sys.argv[1] == 'A':
        print(trees[-1])
    else:
        result = 1
        for tree in trees:
            result = result * tree
        print(result)
