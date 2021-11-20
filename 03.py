from utils import get_puzzle_input, iter_lines
from collections import namedtuple

Claim = namedtuple("Claim", ["id", "pos", "dims"])


def solve_a(inp):
    fabric = {}
    for line in iter_lines(inp):
        if not line.strip() or line == "":
            continue
        claim = parse_line(line)
        x0, x1 = claim.pos
        y0, y1 = claim.dims
        for x in range(x0, x0 + y0):
            for y in range(x1, x1 + y1):
                fabric[(y, x)] = fabric.get((y, x), 0) + 1
    cnt = 0
    for k, v in fabric.items():
        if v >= 2:
            cnt += 1
    print(cnt)


def parse_line(line):
    id_, dims = line.split("@")
    id_, dims = id_.strip(), dims.strip()
    pos, dim = dims.split(":")
    pos = tuple(map(int, pos.strip().split(",")))
    dims = tuple(map(int, dim.strip().split("x")))
    return Claim(id_[1:], pos, dims)


def solve_b(inp):
    fabric_cnt = {}
    fabric_pos = {}
    for line in iter_lines(inp):
        if not line.strip() or line == "":
            continue
        claim = parse_line(line)
        x0, x1 = claim.pos
        y0, y1 = claim.dims
        for x in range(x0, x0 + y0):
            for y in range(x1, x1 + y1):
                fabric_cnt[(y, x)] = fabric_cnt.get((y, x), 0) + 1
                fabric_pos[claim.id] = fabric_pos.get(claim.id, set())
                fabric_pos[claim.id].add((y, x))
    for id_, positions in fabric_pos.items():
        if all([fabric_cnt[(y, x)] == 1 for y, x in positions]):
            print(id_)


if __name__ == "__main__":
    inp = get_puzzle_input("https://adventofcode.com/2018/day/3/input")
    # solve_a(inp)
    solve_b(inp)
