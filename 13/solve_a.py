import sys


def load_stdin():
    # return Path("test").read_text().splitlines()
    return sys.stdin.read().splitlines()

input = load_stdin()

total = 0

board = []
board_transposed = []


def calc(board):
    for i in range(1, len(board)):
        if sum(a != b for a, b in zip(board[i - 1::-1], board[i:])) == 0:
            return i

    return 0


for line in input:
    if not line:
        total += calc(board) * 100
        total += calc(board_transposed)
        board = []
        board_transposed = []
        continue
    board.append(line)
    if not board_transposed:
        board_transposed = ["" for x in line]
    for index, c in enumerate(line):
        board_transposed[index] += c

total += calc(board) * 100
total += calc(board_transposed)

print(total)
