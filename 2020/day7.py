from collections import defaultdict


if __name__ == "__main__":
    bags = {}
    contained_by = defaultdict(list)
    with open('inputs/day7.txt') as f:
        for line in f:
            if line == "\n":
                continue
            line = line.strip().replace('bags', '').replace('bag', '').replace('.', '')
            bag, contains = line.split("contain")
            bag = bag.strip()
            if "no other" in contains:
                bags[bag] = {}
                continue
            contains = contains.split(",")
            contains_dict = {}
            for c in [c.strip() for c in contains]:
                amount = c[:2]
                color = c[2:]
                contains_dict[color] = int(amount)
                contained_by[color].append(bag)
            bags[bag] = contains_dict

    base_parents = {"shiny gold"}
    parents_found = {
        "shiny gold": True
    }
    result = 0
    while True:
        next = set()
        for parent in base_parents:
            parents = contained_by[parent]
            for p in parents:
                if p not in parents_found:
                    parents_found[p] = True
                    next.add(p)
                    result += 1
        if not len(next):
            break
        base_parents = next
    print(result)
    new_bags = {
        "shiny gold": 1
    }
    all_bags = defaultdict(int)  #memoization

    while True:
        next_item = defaultdict(int)
        for bag, value in new_bags.items():
            children = bags[bag]
            for k, v in children.items():
                all_bags[k] += value * v
                next_item[k] += value * v
        if not next_item:
            break
        new_bags = next_item
    print(sum(all_bags.values()))

