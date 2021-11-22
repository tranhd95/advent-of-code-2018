from utils import get_puzzle_input
from collections import deque


inp = get_puzzle_input("https://adventofcode.com/2018/day/8/input")
test = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"

# Part 1
def solve_a(inp):
    inp = map(int, inp.split(" "))
    root = parse(deque(inp))
    print(sum_metadata(root))


def parse(q):
    n_children, n_metadatas = q.popleft(), q.popleft()
    children = [parse(q) for _ in range(n_children)]
    metadatas = [q.popleft() for _ in range(n_metadatas)]
    return children, metadatas


def sum_metadata(node):
    children, metadatas = node
    return sum(metadatas) + sum(sum_metadata(ch) for ch in children)


# Part 1
def solve_b(inp):
    inp = map(int, inp.split(" "))
    root = parse(deque(inp))
    print(node_value(root))


def node_value(node):
    children, metadatas = node
    if children:
        return sum(
            node_value(children[i - 1]) for i in metadatas if 1 <= i <= len(children)
        )
    return sum(metadatas)


solve_a(inp)
solve_b(inp)
