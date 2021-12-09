import re
from typing import final

# Extract the input
f = open('input.txt', 'r')
txt: str = f.read()
f.close()

inpt: list = txt.splitlines()

# These are the numbers that will be called
bingo_nums: list = list(map(int, inpt[0].split(',')))

# These are the boards in their raw state
boards: list = []
# Ignoring the first lines, add the boards in
for i in range(2, len(inpt), 6):
    boards.append(inpt[i:i+5])

# Get a list of the winning combinations
winning_combinations: list = [
    # The winning rows
    list(range(0, 5)),
    list(range(5, 10)),
    list(range(10, 15)),
    list(range(15, 20)),
    list(range(20, 25)),
    # The winning columns
    list(range(0, 21, 5)),
    list(range(1, 22, 5)),
    list(range(2, 23, 5)),
    list(range(3, 24, 5)),
    list(range(4, 25, 5))
]

# Create a board class
class Board:

    def __init__(self, b) -> None:
        # Flatten the board's numbers into a single list
        board_list = []
        for line in b:
            board_list += list(map(int, re.findall('\d*[^\s]', line)))
        self.board = board_list
        self.has_won = False
        self.len_nums_called = 0

    def check_board(self, input_nums):
        """
        Given a board check if it has a line of 5

        Args:
            input_nums (list): The numbers that have been 'called'
        """

        indices = []

        for n in input_nums:
            if n in self.board:
                indices.append(self.board.index(n))

        if not self.has_won:
            for combo in winning_combinations:
                if all(n in indices for n in combo):
                    self.has_won = True
                    self.len_nums_called = len(input_nums)
                    self.score = sum([n if n not in input_nums else 0 for n in self.board]) * input_nums[-1]
                    return True
        return False

final_boards: list = [Board(b) for b in boards]

def part1():
    board_found = False
    for i in range(5, len(bingo_nums)):
        for b in final_boards:
            if b.check_board(bingo_nums[:i]):
                winning_board = b
                nums_called = bingo_nums[:i]
                board_found = True
                break
            else:
                continue
        if board_found:
            break

    return winning_board.score

def part2():

    n_boards_won = 0

    for i in range(5, len(bingo_nums)):
        for b in final_boards:
            if b.check_board(bingo_nums[:i]):
                n_boards_won += 1
            if n_boards_won == 100:
                return b.score
        


print(part2())