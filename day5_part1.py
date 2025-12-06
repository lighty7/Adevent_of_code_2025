from bisect import bisect_right


def parse_input(filename: str):
    with open(filename, "r") as f:
        content = f.read()

    blocks = content.strip().split("\n\n")
    if len(blocks) != 2:
        raise ValueError("Input must contain ranges, a blank line, then IDs.")

    ranges_block = blocks[0].splitlines()
    ids_block = blocks[1].splitlines()

    ranges = []
    for line in ranges_block:
        line = line.strip()
        if not line:
            continue
        lo, hi = line.split("-")
        ranges.append((int(lo), int(hi)))

    ids = [int(line.strip()) for line in ids_block if line.strip()]
    return ranges, ids


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


def is_fresh(x: int, merged_ranges) -> bool:
    if not merged_ranges:
        return False

    starts = [lo for lo, _ in merged_ranges]
    i = bisect_right(starts, x) - 1
    if i < 0:
        return False

    lo, hi = merged_ranges[i]
    return lo <= x <= hi


def count_fresh_ids(filename: str = "input.txt") -> int:
    ranges, ids = parse_input(filename)
    merged = merge_ranges(ranges)

    fresh_count = 0
    for x in ids:
        if is_fresh(x, merged):
            fresh_count += 1

    return fresh_count


if __name__ == "__main__":
    try:
        result = count_fresh_ids("input_day5.txt")
        print(result)
    except Exception as e:
        print("Error:", e)
