
if __name__ == "__main__":
    seats = []
    with open('inputs/day5.txt') as f:
        for line in f:
            s = line.strip()
            row = int(line[:-4].replace("F", "0").replace("B", "1"), 2)
            col = int(line[-4:].replace("L", "0").replace("R", "1"), 2)
            id = row * 8 + col
            seats.append(id)
    missing = len(seats)
    seen = {}
    print(max(seats))
    missing = None
    for i in range(max(seats)):
        if i not in seats:
            missing = i
    print(missing)
