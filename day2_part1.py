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

def sum_invalid_ids(ranges_str):
    ranges = parse_ranges(ranges_str)
    total = 0

    # max ID is 10 digits -> half-length <= 5
    for half_len in range(1, 6):
        start = 10 ** (half_len - 1)
        end = 10 ** half_len
        for half in range(start, end):
            candidate = int(str(half) + str(half))
            if in_ranges(candidate, ranges):
                total += candidate

    return total

if __name__ == "__main__":
    try:
        result = sum_invalid_ids(RANGES_STR)
        print(result)  # 12599655151
    except Exception as e:
        print("Error:", e)
