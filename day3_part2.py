K = 12  # number of batteries to turn on per bank


def max_k_digits(line: str, k: int = K) -> int:
    line = line.strip()
    digits = [int(ch) for ch in line]

    if len(digits) < k:
        raise ValueError(f"Line too short (len={len(digits)}) for k={k}: {line!r}")

    to_remove = len(digits) - k
    stack = []

    for d in digits:
        # Greedily remove smaller digits to the left if we can
        while stack and to_remove > 0 and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    # If still too long, keep only the first k digits
    if len(stack) > k:
        stack = stack[:k]

    # Join first k digits into an integer
    return int("".join(str(x) for x in stack))


def solve(filename: str = "input.txt") -> int:
    total = 0
    with open(filename, "r") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue
            best_for_bank = max_k_digits(line, K)
            total += best_for_bank
    return total


if __name__ == "__main__":
    try:
        result = solve("input5.txt")
        print(result)
    except Exception as e:
        print("Error:", e)
