inst_dict = {
    'E': (0, 0),
    'S': (1, 1),
    'W': (0, 1),
    'N': (1, 0),
}


def check_action(pointer, action, value):
    num = value // 90
    pointer_index = list(inst_dict.values()).index(pointer)
    num = num if action == 'R' else -num
    new_index = list(inst_dict.keys())[(pointer_index + num) % len(inst_dict)]
    return inst_dict[new_index]


def partA(inst):
    ship = [0, 0]
    pointer = (0, 0)
    move = None
    for i in inst:

        action = i[0]
        value = int(i[1:])
        if action in inst_dict:
            move = inst_dict[action]
        elif action == 'F':
            move = pointer
        elif action in ['L', 'R']:
            pointer = check_action(pointer, action, value)
            continue
        else:
            continue
        value = value if not move[1] else -value
        if not move[0] == 0:
            ship[0] += value
        else:
            ship[1] += value
    return abs(ship[0]) + abs(ship[1])


def partB(inst):
    d = ["E", "S", "W", "N"]
    ship = [0, 0]
    way = [10, 1]
    for i in inst:
        action = i[0]
        value = int(i[1:])
        value = -value if action in ["W", "S"] else value
        if action in d:
            if d.index(action) % 2 == 0:
                way[0] += value
            else:
                way[1] += value
        if action == "F":
            ship[0] += way[0] * value
            ship[1] += way[1] * value
        if action in ["L", "R"]:
            value = value // 90
            if action == "R":
                for i in range(value):
                    way[0], way[1] = way[1], -way[0]
            else:
                for i in range(value):
                    way[0], way[1] = -way[1], way[0]
    return abs(ship[0]) + abs(ship[1])


if __name__ == "__main__":
    instructions = [line.strip() for line in open('inputs/day12.txt').readlines()]
    print(partA(instructions))
    print(partB(instructions))