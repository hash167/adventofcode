import re
import sys


all_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
optional_fields = ["cid"]
ecl_allowed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

valid = 0


def validate(k, v):
    if k == "byr":
        if v.isnumeric() and len(v) == 4 and (1920 <= int(v) <= 2002):
            return True
        return False
    if k == "iyr":
        if v.isnumeric() and len(v) == 4 and (2010 <= int(v) <= 2020):
            return True
        return False
    if k == "eyr":
        if v.isnumeric() and len(v) == 4 and (2020 <= int(v) <= 2030):
            return True
        return False
    if k == "hgt":
        if v[-2:] == "cm" and (150 <= int(v[:-2]) <= 193):
            return True
        if v[-2:] == "in" and (59 <= int(v[:-2]) <= 76):
            return True
        return False
    if k == "hcl":
        if v[0] != "#":
            return False
        s = re.search((r'^[a-f0-9]+$'), v[1:])
        try:
            s.group(0)
            return True
        except Exception:
            return False
    if k == "ecl":
        if v in ecl_allowed:
            return True
        else:
            return False
    if k == "pid":
        if v.isnumeric() and len(v) == 9:
            return True
        else:
            return False
    if k == "cid":
        return True
    return False


def check_valid(present):
    global valid
    missing = set(all_fields) - set(present)
    if not missing or missing == set(optional_fields):
        valid += 1


if __name__ == "__main__":
    with open('inputs/day4.txt') as f:
        present = []
        skip = False
        for line in f:
            if line == "\n":
                check_valid(present)
                present = []  # New passport
                skip = False
                continue
            if skip:
                continue
            items = re.split(" +", line.strip())
            for item in items:
                k, v = item.split(":")
                if sys.argv[1] == 'B':
                    skip = not validate(k, v)
                if not skip:
                    present.append(k)
        check_valid(present)
    print(valid)
