import aocd


def parse_input(cookie_id: str) -> list:
    data = aocd.get_data(day=4, year=2022,
                         session=cookie_id)
    lines = data.split("\n")
    return lines


def day_4_1(cookie_id) -> int:
    pairs = parse_input(cookie_id)
    counter = 0
    for pair in pairs:
        elf_1 = [int(x) for x in range(int(pair.split(",")[0].split("-")[0]), int(pair.split(",")[0].split("-")[1])+1)]
        elf_2 = [int(x) for x in range(int(pair.split(",")[1].split("-")[0]), int(pair.split(",")[1].split("-")[1])+1)]
        if all(x in elf_2 for x in elf_1) or all(x in elf_1 for x in elf_2):
            counter += 1
    return counter


def day_4_2(cookie_id) -> int:
    pairs = parse_input(cookie_id)
    counter = 0
    for pair in pairs:
        elf_1 = [int(x) for x in range(int(pair.split(",")[0].split("-")[0]), int(pair.split(",")[0].split("-")[1])+1)]
        elf_2 = [int(x) for x in range(int(pair.split(",")[1].split("-")[0]), int(pair.split(",")[1].split("-")[1])+1)]
        if any(x in elf_2 for x in elf_1):
            counter += 1
    return counter


print(day_4_2("your_cookie_id_here"))