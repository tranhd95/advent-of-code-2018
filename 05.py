from utils import get_puzzle_input


def solve_a(polymer):
    reacted = react(polymer)
    print(len(reacted))


def react(polymer):
    i = 0
    while i < len(polymer) - 1:
        fst = polymer[i]
        snd = polymer[i + 1]
        if abs(ord(fst) - ord(snd)) == 32 and fst.lower() == snd.lower():
            polymer = polymer[0:i] + polymer[i + 2 :]
            i -= 2
            i = max(0, i)
            continue
        i += 1
    return polymer


def solve_b(polymer):
    unique_units = set(polymer.lower())
    lens = set()
    for uu in unique_units:
        removed = remove_unit(uu, polymer)
        lens.add(len(react(removed)))
    print(min(lens))


def remove_unit(unit, polymer):
    result = ""
    for ltr in polymer:
        if ltr.lower() != unit.lower():
            result += ltr
    return result


if __name__ == "__main__":
    inp = get_puzzle_input("https://adventofcode.com/2018/day/5/input")
    # solve_a(inp.strip())
    solve_b(inp.strip())
