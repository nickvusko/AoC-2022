import aocd
from collections import defaultdict


def parse_input(cookie_id: str) -> list:
    data = aocd.get_data(day=5, year=2022,
                         session=cookie_id)
    lines = data.split("\n")
    return lines


def get_columns(list_of_lists: list) -> defaultdict:
    columns = defaultdict(lambda: '')
    for e in range(len(list_of_lists)-1, -1, -1):
        for i in range(0, len(list_of_lists[e]), 4):
            box = list_of_lists[e][i:i + 4]
            if "[" in box:
                columns[int((i + 4) / 4)] += box[1]
    return columns


def day_5_1(cookie_id: str) -> str:
    input_all = parse_input(cookie_id)
    columns = get_columns(input_all[0:8])
    commands = input_all[10:]
    for command in commands:
        what = command.split(" ")
        kolik, odkud, kam = int(what[1]), int(what[3]), int(what[5])
        boxes = columns[odkud]
        moved = boxes[-kolik:]
        moved_to = str(columns[kam]) + moved[::-1]
        left = boxes[:len(boxes)-kolik]
        columns[odkud] = left
        columns[kam] = moved_to
    final_msg = ""
    for i in range(1, 10):
        final_msg += columns[i][-1]
    return final_msg


def day_5_2(cookie_id: str) -> str:
    input_all = parse_input(cookie_id)
    columns = get_columns(input_all[0:8])
    commands = input_all[10:]
    for command in commands:
        what = command.split(" ")
        kolik, odkud, kam = int(what[1]), int(what[3]), int(what[5])
        boxes = columns[odkud]
        moved = boxes[-kolik:]
        moved_to = str(columns[kam]) + moved
        left = boxes[:len(boxes) - kolik]
        columns[odkud] = left
        columns[kam] = moved_to
    final_msg = ""
    for i in range(1, 10):
        final_msg += columns[i][-1]
    return final_msg


print(day_5_2("cookie_id"))
