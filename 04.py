from datetime import datetime

from utils import get_puzzle_input, iter_lines


class Guard:
    def __init__(self, id_):
        self.id = int(id_[1:])
        self.sleep_tbl = {}
        self.last_sleep_date = None
        self.total_sleep = 0

    def sleep(self, date):
        self.last_sleep_date = date

    def wake(self, date):
        if not self.last_sleep_date:
            raise Exception("Already woken.")
        for min in range(self.last_sleep_date.minute, date.minute):
            self.sleep_tbl[min] = self.sleep_tbl.get(min, 0) + 1
        self.total_sleep += abs(self.last_sleep_date.minute - date.minute)
        self.last_sleep_date = None

    def get_sleep_minute(self):
        if not self.sleep_tbl.items():
            return -1, -1
        return max(self.sleep_tbl.items(), key=lambda x: x[1])


def solve_a(inp):
    guards = parse_records(inp)
    guard = max(guards.values(), key=lambda g: g.total_sleep)
    print(
        guard.get_sleep_minute(),
        int(guard.id),
        guard.get_sleep_minute()[0] * int(guard.id),
    )


def parse_records(inp):
    lines = list(iter_lines(inp))
    lines = sorted(lines, key=lambda x: parse_date(x))
    guards = {}
    for l in lines:
        date = parse_date(l)
        if l.endswith("shift"):
            id_ = l.split(" ")[-3]
            if id_ not in guards:
                guards[id_] = Guard(id_)
            guard = guards[id_]
        elif l.endswith("asleep"):
            guard.sleep(date)
        elif l.endswith("up"):
            guard.wake(date)
    return guards


def parse_date(line):
    datestr = " ".join(line.split(" ")[:2])[1:-1]
    return datetime.strptime(datestr, "%Y-%m-%d %H:%M")


def solve_b(inp):
    guards = parse_records(inp)
    chosen = max(guards.values(), key=lambda g: g.get_sleep_minute()[1])
    print(
        chosen.id, chosen.get_sleep_minute(), chosen.id * chosen.get_sleep_minute()[0]
    )


if __name__ == "__main__":
    inp = get_puzzle_input("https://adventofcode.com/2018/day/4/input")
    # solve_a(inp)
    solve_b(inp)
