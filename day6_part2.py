import math


def read_grid(filename: str = "input.txt"):
    with open(filename, "r") as f:
        # keep spaces, strip only newline
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        return []

    width = max(len(line) for line in lines)
    # pad all lines to the same width with spaces
    grid = [line.ljust(width) for line in lines]
    return grid


def find_problem_blocks(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # a separator column is all spaces
    sep = []
    for c in range(cols):
        all_space = True
        for r in range(rows):
            if grid[r][c] != " ":
                all_space = False
                break
        sep.append(all_space)

    blocks = []
    in_block = False
    start = 0

    for c in range(cols):
        if sep[c]:
            if in_block:
                blocks.append((start, c - 1))
                in_block = False
        else:
            if not in_block:
                in_block = True
                start = c

    if in_block:
        blocks.append((start, cols - 1))

    return blocks


def eval_block_cephalopod(grid, start_col, end_col):
    rows = len(grid)
    op_row = rows - 1

    # find operator in bottom row in this block
    op = None
    for c in range(start_col, end_col + 1):
        ch = grid[op_row][c]
        if ch in {"+", "*"}:
            op = ch
            break

    if op is None:
        raise ValueError(f"No operator found in block {start_col}-{end_col}")

    # build numbers from columns, read right-to-left
    numbers = []

    for c in range(end_col, start_col - 1, -1):
        digits = []
        for r in range(op_row):  # rows above operator row
            ch = grid[r][c]
            if ch.isdigit():
                digits.append(ch)
        if not digits:
            # no digits in this column -> not a number column
            continue

        num = int("".join(digits))
        numbers.append(num)

    if not numbers:
        raise ValueError(f"No numbers found in block {start_col}-{end_col}")

    if op == "+":
        return sum(numbers)
    else:  # op == "*"
        return math.prod(numbers)


def solve(filename: str = "input.txt") -> int:
    grid = read_grid(filename)
    blocks = find_problem_blocks(grid)

    total = 0
    for start_col, end_col in blocks:
        total += eval_block_cephalopod(grid, start_col, end_col)

    return total


if __name__ == "__main__":
    try:
        result = solve("input_day6.txt")
        print(result)
    except Exception as e:
        print("Error:", e)
