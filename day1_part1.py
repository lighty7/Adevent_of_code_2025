DIAL_SIZE = 100
START_POSITION = 50

def solve():
    try:
        with open("input.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        current = START_POSITION
        zero_count = 0

        for line in lines:
            direction = line[0]         # 'L' or 'R'
            distance = int(line[1:])

            steps = distance % DIAL_SIZE

            if direction == "L":
                current = (current - steps) % DIAL_SIZE
            elif direction == "R":
                current = (current + steps) % DIAL_SIZE
            else:
                raise ValueError(f"Invalid direction: {line}")

            if current == 0:
                zero_count += 1

        print("Password (times pointing at 0):", zero_count)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    solve()
