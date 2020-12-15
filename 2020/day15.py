def partB(sn, max_turn):
    turn = 0
    prev = 0
    mem = {}
    for b in sn:
        mem[b] = [turn, turn]
        turn += 1
        prev = b
    while turn < max_turn:
        if mem[prev][0] == mem[prev][1]:
            prev = 0
        else:
            prev = mem[prev][1] - mem[prev][0]
        if prev in mem:
            mem[prev][0] = mem[prev][1]
            mem[prev][1] = turn
        else:
            mem[prev] = [turn, turn]
        turn += 1
    return prev


if __name__ == "__main__":
    inputs = [line.strip().split(",") for line in open('inputs/day15.txt').readlines()][0]
    starting_numbers = [int(i) for i in inputs]
    print(partB(starting_numbers, 2020))
    print(partB(starting_numbers, 30000000))