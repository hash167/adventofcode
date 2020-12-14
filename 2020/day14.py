from collections import defaultdict
from itertools import product
from copy import deepcopy


def partA(program):
    mask = ""
    mem = defaultdict(int)
    for inst in program:
        if 'mask' in inst[0]:
            mask = inst[1]
        elif 'mem' in inst[0]:
            addr, val = inst
            addr = int(inst[0][4:-1])
            val = bin(int(inst[1]))[2:].zfill(36)
            res = ""
            for i, m in enumerate(mask):
                if m == 'X':
                    res += val[i]
                else:
                    res += m
            mem[addr] = int(res, 2)
        else:
            print("Encountered illegal operation")
            continue
    return mem
 

def partB(program):
    mask = ""
    mem = defaultdict(int)
    for inst in program:
        if 'mask' in inst[0]:
            mask = inst[1]
        elif 'mem' in inst[0]:
            addr, val = inst
            addr = int(inst[0][4:-1])
            addr_val = bin(addr)[2:].zfill(36)
            res = ""
            for i, m in enumerate(mask):
                if m == '0':
                    res += addr_val[i]
                else:
                    res += m
            num_float = res.count('X')
            combs = product('01', repeat=num_float)
            res_list = []
            for comb in combs:
                items = list(comb)
                res_copy = deepcopy(res)
                while items:
                    item = items.pop()
                    res_copy = res_copy.replace('X', item, 1)
                res_list.append(res_copy)
            for r in res_list:
                mem[int(r, 2)] = int(val)
        else:
            print("Encountered illegal operation")
            continue
    return mem


if __name__ == "__main__":
    program = [line.strip().split(" = ") for line in open('inputs/day14.txt').readlines()]
    sum = 0
    for k, v in partA(program).items():
        if v != 0:
            sum += v
    print(sum)
    sum_b = 0
    for k, v in partB(program).items():
        if v != 0:
            sum_b += v
    print(sum_b)