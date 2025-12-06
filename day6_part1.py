import math
import re


def read_grid(filename: str = "input.txt"):
    with open(filename, "r") as f:
        # Only strip the newline, keep spaces (important!)
        lines = [line.rstrip("\n") for line in f]

    if not lines:
        return []

    width = max(len(line) for line in lines)
    # Pad all lines to same width with spaces
    grid = [line.ljust(width) for line in lines]
    return grid


def find_problem_blocks(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # A separator column is all spaces
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


def eval_block(grid, start_col, end_col):
    rows = len(grid)
    op_row = rows - 1

    # Find operator in the last row within this block
    op = None
    for c in range(start_col, end_col + 1):
        ch = grid[op_row][c]
        if ch in {"+", "*"}:
            op = ch
            break

    if op is None:
        raise ValueError(f"No operator found in block {start_col}-{end_col}")

    numbers = []
    # All rows above last row contain the numbers
    for r in range(op_row):
        slice_ = grid[r][start_col:end_col + 1]
        # Extract contiguous digit groups
        for token in re.findall(r"\d+", slice_):
            numbers.append(int(token))

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
        total += eval_block(grid, start_col, end_col)
    return total


if __name__ == "__main__":
    try:
        result = solve("input_day6.txt")
        print(result)
    except Exception as e:
        print("Error:", e)
