DIAL_SIZE = 100
START_POSITION = 50


def solve_method_434C49434B(filename="input1.txt"):
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]

        current = START_POSITION
        zero_count = 0

        for line in lines:
            direction = line[0]          # 'L' or 'R'
            distance = int(line[1:])     # do NOT mod by 100 here

            if direction == "L":
                delta = -1
            elif direction == "R":
                delta = 1
            else:
                raise ValueError(f"Invalid direction in line: {line}")

            # simulate click-by-click
            for _ in range(distance):
                current = (current + delta) % DIAL_SIZE
                if current == 0:
                    zero_count += 1

        print("Password (method 0x434C49434B):", zero_count)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    solve_method_434C49434B()
