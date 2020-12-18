from collections import defaultdict
def partB(sn, max_turn):
    turn = 0
    prev = 0
    mem = {}
    for b in sn:
        mem[b] = turn
        prev = b
        turn += 1
    while turn < max_turn:
        val = None
        if prev in mem:
            val = (turn - 1) - mem[prev]
        else:
            val = 0
        if prev >= 0:
            mem[prev] = turn - 1 
        prev = val
        turn += 1
    return prev


def partB_concise(sn, max_turn):
    last_seen = defaultdict(lambda: i, {c: i for i, c in enumerate(sn[:-1])})
    last = sn[-1]
    turn = len(sn) - 1
    for i in range(turn, max_turn - 1):
        last_seen[last], last = i, i - last_seen[last]
    return last


if __name__ == "__main__":
    inputs = [line.strip().split(",") for line in open('inputs/day15.txt').readlines()][0]
    starting_numbers = [int(i) for i in inputs]
    print(partB_concise(starting_numbers, 2020))
    print(partB_concise(starting_numbers, 30000000))