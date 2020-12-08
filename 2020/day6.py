from functools import reduce

if __name__ == "__main__":
    result_a = 0
    result_b = 0
    with open('inputs/day6.txt') as f:
        ans_a = set()
        ans_b = []
        for line in f:
            if line == "\n":
                result_a += len(ans_a)
                # bitwise and operation on set gives us interesctions
                common = reduce(lambda x, y: x & y, ans_b)
                result_b += len(common)
                ans_a = set()
                ans_b = []
                continue
            s = line.strip()
            ans_a.update(list(s))
            ans_b.append(set(list(s)))
    print(result_a)
    print(result_b)
