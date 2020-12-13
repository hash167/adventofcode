from copy import deepcopy


deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def count_seated(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i, j in deltas:
        xi, xj = r + i, c + j
        if 0 <= xi < rows and 0 <= xj < cols and grid[xi][xj] == '#':
            count += 1
    return count


def partA(seats):
    while True:
        seated = 0
        copy_seats = deepcopy(seats)
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                count = count_seated(i, j, copy_seats)
                if copy_seats[i][j] == 'L':
                    if count == 0:
                        seats[i][j] = '#'
                        seated += 1
                elif copy_seats[i][j] == '#':
                    if count < 4:
                        seated += 1
                    else:
                        seats[i][j] = 'L'
                else:
                    continue
        if copy_seats == seats:
            return seated
    return 0


def count_seated_2(r, c, grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i, j in deltas:
        xi, xj = r + i, c + j
        while 0 <= xi < rows and 0 <= xj < cols:
            if grid[xi][xj] == '#':
                count += 1
                break
            elif grid[xi][xj] == 'L':
                break
            xi += i
            xj += j
    return count


def partB(seats):
    while True:
        copy_seats = deepcopy(seats)
        for i in range(len(seats)):
            for j in range(len(seats[0])):
                count = count_seated_2(i, j, copy_seats)
                if copy_seats[i][j] == 'L' and count == 0:
                    seats[i][j] = '#'
                elif copy_seats[i][j] == '#' and count >= 5:
                    seats[i][j] = 'L'
                else:
                    continue
        if copy_seats == seats:
            seated = 0
            for m in range(len(seats)):
                for n in range(len(seats[0])):
                    if copy_seats[m][n] == '#':
                        seated += 1
            return seated
    return 0


if __name__ == "__main__":
    seats = [list(line.strip())
             for line in open('inputs/day11.txt').readlines()]
    copy_seats = deepcopy(seats)
    print(partA(seats))
    print(partB(copy_seats))
