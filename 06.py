from utils import get_puzzle_input, iter_lines


def solve_a(inp):
    targets = {tuple(map(int, t.split(", "))) for t in iter_lines(inp)}
    min_x, max_x = min(x for x, y in targets), max(x for x, y in targets)
    min_y, max_y = min(y for x, y in targets), max(y for x, y in targets)
    cnt = {}
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            fst, snd = sorted((dist((x, y), t), i) for i, t in enumerate(targets))[:2]
            if fst[0] != snd[0]:
                cnt[fst[1]] = cnt.get(fst[1], 0) + 1
    for i, (x, y) in enumerate(targets):
        if x == min_x or x == max_x or y == min_y or y == max_y:
            del cnt[i]
    print(max(cnt.values()))


def dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def solve_b(inp):
    targets = {tuple(map(int, t.split(", "))) for t in iter_lines(inp)}
    min_x, max_x = min(x for x, y in targets), max(x for x, y in targets)
    min_y, max_y = min(y for x, y in targets), max(y for x, y in targets)
    region = 0
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if sum(dist((x, y), (t)) for t in targets) < 10_000:
                region += 1
    print(region)


if __name__ == "__main__":
    inp = get_puzzle_input("https://adventofcode.com/2018/day/6/input")
    # solve_a(inp.strip())
    solve_b(inp.strip())
