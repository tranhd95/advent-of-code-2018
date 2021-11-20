from utils import get_puzzle_input, iter_lines
from collections import Counter
from itertools import islice


def solve_a(inp):
    two, three = 0, 0
    for box in iter_lines(inp):
        cnt = Counter(str(box).strip())
        if 2 in cnt.values():
            two += 1
        if 3 in cnt.values():
            three += 1
    print(two * three)


def solve_b(inp):
    for box1 in iter_lines(inp):
        for box2 in islice(iter_lines(inp), 1, None):
            if common := get_common_if_close(box1, box2):
                print(common)
                return


def get_common_if_close(box1, box2):
    common = []
    cnt_diff = 0
    for l1, l2 in zip(box1, box2):
        if cnt_diff >= 2:
            return None
        if l1 == l2:
            common.append(l1)
        else:
            cnt_diff += 1
    return "".join(common) if cnt_diff != 0 else None


if __name__ == "__main__":
    inp = get_puzzle_input("https://adventofcode.com/2018/day/2/input")
    # solve_a(inp)
    solve_b(inp)
