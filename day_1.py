
def parse_input(fh: str) -> list:
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    print(lines)
    return lines


def day_1_1(file: str) -> str:
    lines = parse_input(file)
    elf = 1
    calories = {f"elf_{elf}": 0}
    for row in lines:
        if row != "":
            calories[f"elf_{elf}"] += int(row)
        else:
            elf += 1
            calories[f"elf_{elf}"] = 0
    return f"{max(calories, key=calories.get)} has {max(calories.values())} calories in his tiny bag."


def day_1_2(file: str) -> str:
    lines = parse_input(file)
    elf = 1
    calories = {f"elf_{elf}": 0}
    for row in lines:
        if row != "":
            calories[f"elf_{elf}"] += int(row)
        else:
            elf += 1
            calories[f"elf_{elf}"] = 0
    elves = sorted(calories, key=calories.get, reverse=True)[:3]
    total = calories[elves[0]] + calories[elves[1]] + calories[elves[2]]
    return f"Top three elves have {total} calories in their tiny bag."


print(day_1_2("input"))
