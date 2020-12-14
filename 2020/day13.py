def partA(ts, bus_ids):
    min = float('inf')
    bus_min = 0
    for id in bus_ids:
        diff = id - (ts % id)
        if diff < min:
            bus_min = id
            min = diff
    return min * bus_min


def partB(busses):
    step = 1
    min_val = busses[0][1]
    for i, bus in busses[1:]:
        while (min_val+i) % bus != 0:
            min_val += step
        step *= bus
    return min_val


if __name__ == "__main__":
    inputs = [line.strip() for line in open('inputs/day13.txt').readlines()]
    time_stamp = int(inputs[0])
    bus_ids = [int(id) for id in inputs[1].split(',') if id != 'x']
    bus_offsets = [(i, int(b)) for i, b in enumerate(inputs[1].split(',')) if b != 'x']
    print(partA(time_stamp, bus_ids))
    print(partB(bus_offsets))