def parse_ranges(filename: str):
    with open(filename, "r") as f:
        content = f.read()

    blocks = content.strip().split("\n\n")
    if not blocks:
        raise ValueError("Empty input")

    ranges_block = blocks[0].splitlines()

    ranges = []
    for line in ranges_block:
        line = line.strip()
        if not line:
            continue
        lo, hi = line.split("-")
        ranges.append((int(lo), int(hi)))

    return ranges


def merge_ranges(ranges):
    if not ranges:
        return []

    ranges.sort()  # sort by start, then end
    merged = []
    cur_lo, cur_hi = ranges[0]

    for lo, hi in ranges[1:]:
        if lo <= cur_hi + 1:
            cur_hi = max(cur_hi, hi)
        else:
            merged.append((cur_lo, cur_hi))
            cur_lo, cur_hi = lo, hi

    merged.append((cur_lo, cur_hi))
    return merged


def count_all_fresh_ids(filename: str = "input.txt") -> int:
    ranges = parse_ranges(filename)
    merged = merge_ranges(ranges)

    total = 0
    for lo, hi in merged:
        total += (hi - lo + 1)
    return total


if __name__ == "__main__":
    try:
        result = count_all_fresh_ids("input_day5.txt")
        print(result)
    except Exception as e:
        print("Error:", e)
