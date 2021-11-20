import requests

from utils import get_puzzle_input, gen_line
from itertools import cycle


def solve_a(inp):
    result = 0
    for delta in gen_line(inp):
        if not delta:
            continue
        result += int(delta)
    print(result)


def solve_b(inp):
    result = 0
    seen = set()
    for delta in cycle(gen_line(inp)):
        if not delta:
            continue
        result += int(delta)
        if result in seen:
            print(result)
            return
        else:
            seen.add(result)


if __name__ == "__main__":
    inp = get_puzzle_input("https://adventofcode.com/2018/day/1/input")
    solve_a(inp)
    solve_b(inp)
