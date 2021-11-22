import re
import os

from utils import get_puzzle_input, iter_lines

VEC_RE = re.compile(r"(-?\d+)")


def solve(inp):
    positions, v = [], []
    for line in iter_lines(inp):
        p1, p2, v1, v2 = tuple(map(int, VEC_RE.findall(line)))
        positions.append((p1, p2))
        v.append((v1, v2))
    t = 0
    while True:
        for i in range(len(positions)):
            x0, y0 = positions[i]
            v1, v2 = v[i]
            positions[i] = (x0 + v1, y0 + v2)
        if display(positions):
            print("time elapsed:", t)
            input()
            os.system("cls" if os.name == "nt" else "clear")
        t += 1


def get_bbox(positions):
    x_min, x_max = min(x for x, y in positions), max(x for x, y in positions)
    y_min, y_max = min(y for x, y in positions), max(y for x, y in positions)
    return x_min, x_max, y_min, y_max


def display(positions):
    x_min, x_max, y_min, y_max = get_bbox(positions)
    area = (x_max - x_min) * (y_max - y_min)
    if area <= 1000:
        for y in range(y_min - 2, y_max + 2):
            for x in range(x_min - 2, x_max + 2):
                if (x, y) in positions:
                    print("X", end="")
                else:
                    print(".", end="")
            print()
        return True
    return False


solve(get_puzzle_input("https://adventofcode.com/2018/day/10/input"))
