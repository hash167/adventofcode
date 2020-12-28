import itertools
from collections import defaultdict

# Not needed but added it, just in case it was
def combine_ranges(sorted_ranges):
    res = [sorted_ranges[0]]
    for i in range(1, len(sorted_ranges)):
        prev = res.pop()
        if prev[1] >= sorted_ranges[i][0]:
            if prev[1] >= sorted_ranges[i][1]:
                res.append(prev)
            else:
                res.append([prev[0], sorted_ranges[i][1]])
        else:
            res.append(prev)
            res.append(sorted_ranges[i])
    return res


def in_range(item: int, el_list: list) -> bool:
    inrange = False
    for el in el_list:
        # print(el)
        if el[0] <= item <= el[1]:
            inrange = True
    return inrange


def partA(rules, my, nearby):
    ranges = list(itertools.chain.from_iterable(rules.values()))
    ranges = sorted(ranges, key=lambda x: x[0])
    ranges = combine_ranges(ranges)
    invalid = []
    valid = []
    for n in nearby:
        valid_ticket = True
        for i in n:
            if i in invalid or not in_range(i, ranges):
                invalid.append(i)
                valid_ticket = False
                break
        if valid_ticket:
            valid.append(n)
    print(invalid)
    return invalid, valid


def check_invalid_pos(pos_values, ranges):
    invalid = False
    for item in pos_values:
        if not in_range(item, ranges):
            invalid = True
            break
    return invalid


def partB(rules, my, valid):
    values_at_pos = defaultdict(list)
    for ticket in valid:
        for i, num in enumerate(ticket):
            values_at_pos[i].append(num)
    rules_mapping = defaultdict(dict)
    for pos, values in values_at_pos.items():
        for name, ranges in rules.items():
            if check_invalid_pos(values, ranges):
                continue
            rules_mapping[name][pos] = True
    result = {}
    while rules_mapping:
        single = [{name: list(v.keys())[0]} for name, v in rules_mapping.items() if len(v) == 1 ]
        print(single)
        for name, pos in rules_mapping.copy().items():
            if len(pos) != 1:
                continue
            p = list(pos.keys())[0]
            result[name] = p
            del rules_mapping[name]
            for key, val in rules_mapping.items():
                if p in val:
                    del val[p]

    prod = 1
    for name, index in result.items():
        if 'departure' in name:
            prod *= my[index]
    return prod



if __name__ == "__main__":
    section = 0
    my_ticket = []
    nearby_tickets = []
    rules = {}
    with open('inputs/day16.txt') as f:
        for line in f:
            if not line.strip():
                continue
            if line.strip() == "your ticket:":
                section += 1
                continue
            elif line.strip() == "nearby tickets:":
                section += 1
                continue
            if section == 0:
                rule_id, values = line.strip().split(": ")
                values = values.split(' or ')
                values = [[int(i) for i in v.split('-')] for v in values]
                rules[rule_id] = values
            if section == 1:
                my_ticket = [int(v) for v in line.strip().split(',')]
            if section == 2:
                nearby_tickets.append([int(v) for v in line.strip().split(',')])
    invalid_set, valid = partA(rules, my_ticket, nearby_tickets)
    print(sum(invalid_set))
    print(partB(rules, my_ticket, valid))
