import sys
import copy

file = open('./input.txt', 'r')
lines = file.readlines()
file.close()

guesses = lines[0].strip().split(',')
lines = lines[2:]
COL_SIZE = 5
ROW_SIZE = 5

def is_solved_for_rows(board_mask):
    for row in range(ROW_SIZE):
        marked_count = 0
        for col in range(COL_SIZE):
            if board_mask[row][col] is not True:
                break
            marked_count += 1
            if marked_count == COL_SIZE:
                return True
    return False

def is_solved_for_columns(board_mask):
    for col in range(COL_SIZE):
        marked_count = 0
        for row in range(ROW_SIZE):
            if board_mask[row][col] is not True:
                break
            marked_count += 1
            if marked_count == ROW_SIZE:
                return True
    return False

def is_solved(board_mask):
    return is_solved_for_rows(board_mask) or is_solved_for_columns(board_mask)

def get_unmarked(board, board_mask):
    unmarked = []
    for row in range(ROW_SIZE):
        for col in range(COL_SIZE):
            if board_mask[row][col] is not True:
                unmarked.append(board[row][col])
    return unmarked

def get_boards(lines):
    board = []
    boards = []
    for line in lines:
        if not line.strip():
            if board:
                boards.append(board)
            board = []
            continue
        line = line.strip().replace('  ', ' ').split(' ')
        board.append(line)
    boards.append(board)
    return boards

boards = get_boards(lines)
boards_masks = copy.deepcopy(boards)
won_boards = set()

for guess in guesses:
    for bi in range(len(boards)):
        for row in range(ROW_SIZE):
            for col in range(COL_SIZE):
                if boards[bi][row][col] == guess:
                    boards_masks[bi][row][col] = True
        if is_solved(boards_masks[bi]):
            won_boards.add(bi)
            if len(won_boards) == len(boards):
                unmarked_sum = sum([int(num) for num in get_unmarked(boards[bi], boards_masks[bi])])
                guess = int(guess)
                print(f"Last guess: {guess}, sum of unmarked numbers: {unmarked_sum}, result: ", unmarked_sum * guess) #13884
                sys.exit()