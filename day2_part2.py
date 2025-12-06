RANGES_STR = (
    "3335355312-3335478020,62597156-62638027,94888325-95016472,"
    "4653-6357,54-79,1-19,314-423,472-650,217886-298699,"
    "58843645-58909745,2799-3721,150748-178674,9084373-9176707,"
    "1744-2691,17039821-17193560,2140045-2264792,743-1030,"
    "6666577818-6666739950,22946-32222,58933-81008,"
    "714665437-714803123,9972438-10023331,120068-142180,101-120,"
    "726684-913526,7575737649-7575766026,8200-11903,81-96,"
    "540949-687222,35704-54213,991404-1009392,335082-425865,"
    "196-268,3278941-3383621,915593-991111,32-47,431725-452205"
)


def parse_ranges(ranges_str):
    ranges = []
    for part in ranges_str.split(","):
        part = part.strip()
        if not part:
            continue
        lo, hi = part.split("-")
        ranges.append((int(lo), int(hi)))
    return ranges


def in_ranges(x, ranges):
    for lo, hi in ranges:
        if lo <= x <= hi:
            return True
    return False


def generate_repeated_max_len(max_len=10):
    nums = set()

    # period_len is length of base block t
    for period_len in range(1, max_len + 1):
        # k is how many times t is repeated; need at least 2 repeats
        for k in range(2, max_len // period_len + 1):
            start = 10 ** (period_len - 1)   # no leading zero
            end = 10 ** period_len

            for t in range(start, end):
                s = str(t) * k
                if len(s) > max_len:
                    break

                n = int(s)
                nums.add(n)

    return nums


def sum_invalid_ids(ranges_str):
    ranges = parse_ranges(ranges_str)
    candidates = generate_repeated_max_len(10)

    total = 0
    for n in candidates:
        if in_ranges(n, ranges):
            total += n

    return total


if __name__ == "__main__":
    try:
        result = sum_invalid_ids(RANGES_STR)
        print(result)   # 20942028255
    except Exception as e:
        print("Error:", e)
