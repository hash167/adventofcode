from collections import defaultdict, namedtuple

Coord = namedtuple('Coord', ['X', 'Y', 'Z'])


def find_neighbors(c):
    neighbors = [Coord(c[0]+i, c[1]+j, c[2]+k)
                 for i in range(-1, 2)
                 for j in range(-1, 2)
                 for k in range(-1, 2)
                 if not (i == 0 and j == 0 and k == 0)]
    return neighbors


def step(prev_active):
    active_neighbors = defaultdict(int)
    for coord in prev_active:
        if coord not in active_neighbors:
            active_neighbors[coord] = 0
        for neighbor in find_neighbors(coord):
            active_neighbors[neighbor] += 1
    new_active = []
    for coord, active_neighbor_count in active_neighbors.items():
        if coord in prev_active:
            if active_neighbor_count in [2, 3]:
                new_active.append(coord)
        else:
            if active_neighbor_count == 3:
                new_active.append(coord)
    return new_active


def partA(prev_active):
    for _ in range(6):
        prev_active = step(prev_active)

    return len(prev_active)


if __name__ == "__main__":
    active = []
    with open('inputs/day17.txt') as f:
        for i, line in enumerate(f):
            for j, c in enumerate(list(line.strip())):
                if c == "#":
                    active.append(Coord(i, j, 0))
        # print(active, len(active))
        print(partA(active))

