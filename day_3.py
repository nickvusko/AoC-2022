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


def day_3_2(file: str):
    letters_lower = {key: ord(f"{key}")-96 for key in string.ascii_lowercase}
    letters_upper = {key: ord(f"{key}")-38 for key in string.ascii_uppercase}
    all_letters = {**letters_lower, **letters_upper}
    bags = parse_input(file)
    badges = []
    for i in range(0, len(bags), 3):
        group = bags[i:i+3]
        common = dict.fromkeys(all_letters.keys(), 0)
        for bag in group:
            letter_tracker = []
            for letter in bag:
                if letter not in letter_tracker:
                    letter_tracker.append(letter)
                    common[letter] += 1
        badges.append(max(common, key=common.get))
    total_value = 0
    for found in badges:
        total_value += all_letters[found]
    return total_value


print(day_3_2("input"))
