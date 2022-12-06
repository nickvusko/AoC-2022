import aocd


def parse_input(cookie_id: str) -> list:
    data = aocd.get_data(day=6, year=2022,
                         session=cookie_id)
    return data


def day_6_1(cookie_id: str):
    stream = parse_input(cookie_id)
    received_letters = set()
    position = 0
    while len(received_letters) < 4:
        received_letters = set(stream[position:position+4])
        position += 1
    return position+3


def day_6_2(cookie_id: str):
    stream = parse_input(cookie_id)
    received_letters = set()
    position = 0
    while len(received_letters) < 14:
        received_letters = set(stream[position:position+14])
        position += 1
    return position+13


print(day_6_2("cookie_id"))