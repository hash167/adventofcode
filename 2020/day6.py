from functools import reduce

if __name__ == "__main__":
    next = False
    result = 0
    result_b = 0
    with open('inputs/day6.txt') as f:
        ans = set()
        ans_b = []
        for line in f:
            if line == "\n":
                result += len(ans)
                common = reduce(lambda x, y: x & y, ans_b)
                result_b += len(common)
                ans = set()
                ans_b = []
                continue
            s = line.strip()
            ans.update(list(s))
            ans_b.append(set(list(s)))
    print(result)
    print(result_b)
