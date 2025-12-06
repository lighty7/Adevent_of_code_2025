from collections import deque


def total_removable_rolls(filename: str = "input.txt") -> int:
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f if line.strip()]

    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    # 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1),
    ]

    # Neighbor count for each @
    neighbor_count = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "@":
                continue
            cnt = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == "@":
                        cnt += 1
            neighbor_count[r][c] = cnt

    q = deque()

    # Initial accessible rolls
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "@" and neighbor_count[r][c] < 4:
                q.append((r, c))

    removed = 0

    while q:
        r, c = q.popleft()

        # Might have been removed already
        if grid[r][c] != "@":
            continue

        # If for some reason it no longer qualifies, skip
        if neighbor_count[r][c] >= 4:
            continue

        # Remove this roll
        grid[r][c] = "."
        removed += 1

        # Update neighbors
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == "@":
                    neighbor_count[nr][nc] -= 1
                    if neighbor_count[nr][nc] < 4:
                        q.append((nr, nc))

    return removed


if __name__ == "__main__":
    try:
        result = total_removable_rolls("input7.txt")
        print(result)
    except Exception as e:
        print("Error:", e)
