def max_two_digit_from_line(line: str) -> int:
    line = line.strip()
    if len(line) < 2:
        # Can't form any two-digit number
        raise ValueError(f"Line too short to form a number: {line!r}")

    digits = [int(ch) for ch in line]  # digits 1-9

    n = len(digits)
    suffix_max = [None] * n

    # Build suffix max "to the right"
    current_max = -1
    for i in range(n - 1, -1, -1):
        suffix_max[i] = current_max
        if digits[i] > current_max:
            current_max = digits[i]

    best = -1
    for i in range(n - 1):  # last index can't be the first digit of a pair
        right_max = suffix_max[i]
        if right_max == -1:  # no digit to the right
            continue
        candidate = 10 * digits[i] + right_max
        if candidate > best:
            best = candidate

    if best == -1:
        raise ValueError(f"No two-digit number could be formed from line: {line!r}")

    return best


def solve(filename: str = "input.txt") -> int:
    total = 0
    with open(filename, "r") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:  # skip empty lines if any
                continue
            max_for_line = max_two_digit_from_line(line)
            total += max_for_line
    return total


if __name__ == "__main__":
    try:
        result = solve("input5.txt")
        print(result)
    except Exception as e:
        print("Error:", e)
