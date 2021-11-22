from utils import get_puzzle_input, iter_lines
from collections import defaultdict


def solve_a(inp):
    dag = DAG()
    for line in iter_lines(inp):
        splits = line.split(" ")
        s, t = splits[1], splits[-3]
        dag.add_edge(s, t)
    print(dag.get_order())


class DAG:
    def __init__(self):
        self.deps = defaultdict(set)
        self.V = set()

    def add_edge(self, src, target):
        self.deps[target].add(src)
        self.V |= {src, target}

    def get_order(self):
        order = ""
        for _ in self.V:
            order += min(
                v for v in self.V if v not in order and self.deps[v] <= set(order)
            )
        return order


def solve_b(inp):
    tasks = set()
    deps = defaultdict(set)
    for line in iter_lines(inp):
        splits = line.split(" ")
        s, t = splits[1], splits[-3]
        tasks |= {s, t}
        deps[t].add(s)
    seconds = 0
    works = [""] * 2
    timers = [0] * 2
    done = set()
    while True:
        for i, t in enumerate(timers):
            times_up = t == 1
            if times_up:
                done.add(works[i])
            timers[i] = max(0, t - 1)
        while 0 in timers:
            i = timers.index(0)
            next_tasks = [
                t
                for t in tasks
                if (t not in done) and (t not in works) and (deps[t] <= set(done))
            ]
            if not next_tasks:
                break
            works[i] = next_tasks[0]
            timers[i] = ord(next_tasks[0]) - ord("A") + 1
        if sum(timers) == 0:
            break
        seconds += 1
    print(seconds)


if __name__ == "__main__":
    inp = get_puzzle_input("https://adventofcode.com/2018/day/7/input")
    # solve_a(inp)
    solve_b(inp)
