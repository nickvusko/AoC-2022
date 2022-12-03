
def parse_input(fh: str) -> list:
    with open(f"{fh}.txt") as f:
        lines = [x.strip("\n") for x in f.readlines()]
    print(lines)
    return lines


def day_2_1(file: str, guide: dict) -> int:
    rows = parse_input(file)
    total_score = 0
    win = ["C X", "B Z", "A Y"]
    for row in rows:
        not_me, me = row.split(" ")
        if row in win:
            total_score += guide[me] + 6
        elif guide[not_me] == guide[me]:
            total_score += (3 + guide[me])
        else:
            total_score += guide[me]
    return total_score


def day_2_2(file: str, loss: dict, won: dict, guide: dict) -> int:
    rows = parse_input(file)
    total_score = 0
    for row in rows:
        not_me, result = row.split(" ")
        if result == "Z":
            total_score += guide[won[not_me]] + 6
        elif result == "Y":
            total_score += guide[not_me] + 3
        else:
            total_score += guide[loss[not_me]]
    return total_score


values_1 = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
values_l = {"A": "Z", "B": "X", "C": "Y"}
values_w = {"A": "Y", "B": "Z", "C": "X"}
print(day_2_2("input", values_l, values_w, values_1))
