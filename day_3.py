import string

def parse_input(fh: str) -> list:
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    return lines


def day_3_1(file: str):
    letters_lower = {key: ord(f"{key}")-96 for key in string.ascii_lowercase}
    letters_upper = {key: ord(f"{key}")-38 for key in string.ascii_uppercase}
    all_letters = {**letters_lower, **letters_upper}
    bags = parse_input(file)
    ups = []
    for bag in bags:
        ups_local = []
        middle = int(len(bag)/2)
        st_comp = bag[0:middle]
        nd_comp = bag[middle:]
        for e in st_comp:
            if e in nd_comp and e not in ups_local:
                ups_local.append(e)
                ups.append(e)
        for i in nd_comp:
            if i in st_comp and i not in ups_local:
                ups_local.append(i)
                ups.append(i)
    total_value = 0
    print(ups)
    for problem in ups:
        total_value += all_letters[problem]
    return total_value


print(day_3_1("input"))



