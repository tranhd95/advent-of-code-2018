from collections import deque


def solve(players, marbles):
    board = deque([0])
    scores = [0] * players
    for new_marble in range(1, marbles + 1):
        if new_marble % 23 == 0:
            board.rotate(7)
            scores[new_marble % players] += board.pop() + new_marble
            board.rotate(-1)
        else:
            board.rotate(-1)
            board.append(new_marble)
    return max(scores)


# print(solve(466, 71436))
print(solve(466, 71436 * 100))
