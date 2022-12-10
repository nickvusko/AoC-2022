import aocd
import numpy as np


def parse_input(cookie_id: str) -> np.array:
    data = aocd.get_data(day=8, year=2022,
                         session=cookie_id)
    lines = data.split("\n")
    array = np.array([list(x) for x in lines])
    return array


def day_8_1(cookie_id: str):
    forest = parse_input(cookie_id)
    visible = 2*forest.shape[0] + 2 * forest.shape[1] - 4
    for i in range(1, forest.shape[0]-1):
        for e in range(1, forest.shape[1]-1):
            if look_left(i, e, forest[i][e], forest)[0] or look_right(i, e, forest[i][e], forest)[0] \
                    or look_up(i, e, forest[i][e], forest)[0] or look_down(i, e, forest[i][e], forest)[0]:
                visible += 1
    return visible


def day_8_2(cookie_id: str):
    forest = parse_input(cookie_id)
    visible_total = 0
    for i in range(0, forest.shape[0]-1):
        for e in range(0, forest.shape[1] - 1):
            trees = [look_left(i, e, forest[i][e], forest)[1], look_right(i, e, forest[i][e], forest)[1],
                     look_up(i, e, forest[i][e], forest)[1], look_down(i, e, forest[i][e], forest)[1]]
            print(trees, i, e)
            try:
                trees.remove(0)
            except ValueError:
                print("no zeros in list")
            visible = trees[0]
            for f in range(1, len(trees)):
                visible = visible*trees[f]
            if visible > visible_total:
                visible_total = visible
    return visible_total


def look_left(pos_x, pos_y,  value, array):
    count = 0
    if pos_x == 0:
        return False, count
    for i in range(pos_x-1, -1, -1):
        count += 1
        if value > array[i][pos_y]:
            continue
        else:
            return False, count
    return True, count


def look_right(pos_x, pos_y, value, array):
    count = 0
    if pos_x == array.shape[0]-1:
        return False, count
    for i in range(pos_x+1, array.shape[0]):
        count += 1
        if value > array[i][pos_y]:
            continue
        else:
            return False, count
    return True, count


def look_up(pos_x, pos_y, value, array):
    count = 0
    if pos_y == 0:
        return False, count
    for i in range(pos_y-1, -1, -1):
        count += 1
        if value > array[pos_x][i]:
            continue
        else:
            return False, count
    return True, count


def look_down(pos_x, pos_y, value, array):
    count = 0
    if pos_y == array.shape[1]-1:
        return False, count
    for i in range(pos_y+1, array.shape[1]):
        count += 1
        if value > array[pos_x][i]:
            continue
        else:
            return False, count
    return True, count


print(day_8_2("53616c7465645f5ffbea5dcfe36a2b2113abe09c4efe4073649cb1ac4194014fd3c6330a3e058a20bbe56f19bb8e79f6528507d07d03099fb8c3d7bc8ab9ec5d"))
