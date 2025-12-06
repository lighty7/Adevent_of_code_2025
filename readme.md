# Advent of Code Solutions (Days 1–6)

This repository contains clean and efficient solutions for Advent of Code puzzles, written in **Python** and organized by day and part.

Each day has:

* Problem description summary
* Approach / reasoning
* Final working code

---

## Day 1: Secret Entrance

### Part 1

* Simulate dial rotations.
* Count how many times dial points at **0** after each rotation.

### Part 2

* Count **every click landing on 0**, not only at the end.
* No `% 100` optimization here, since full rotations count.

---

## Day 2: Gift Shop

### Part 1

* Find numbers made by **repeating a digit sequence twice**.
* Check if they fall inside the given ranges.
* Sum them.

### Part 2

* Same, but digit sequence **repeated at least twice** (2–7 repeats).

---

## Day 3: Lobby

### Part 1

* For each line of digits, find the **largest 2-digit number** using ordered positions.
* Sum per-line maxima.

### Part 2

* Choose **exactly 12 digits** from each line.
* Maintain order.
* Use greedy **monotonic stack**.

---

## Day 4: Printing Department

### Part 1

* Grid of `@` rolls.
* A roll is accessible if it has **< 4 neighbors** in 8 directions.
* Count accessible.

### Part 2

* Remove accessible rolls iteratively.
* Removing reduces neighbors.
* Use queue (graph core removal).
* Output total removed.

---

## Day 5: Cafeteria

### Part 1

* Ranges + IDs.
* Merge ranges.
* Count how many IDs fall inside any range.

### Part 2

* Ignore IDs.
* Merge ranges.
* Sum `(hi - lo + 1)` for all merged.

---

## Day 6: Trash Compactor

### Part 1

* Worksheet of vertically-arranged problems.
* Blocks separated by **blank columns**.
* Evaluate each block, add totals.

### Part 2

* **Cephalopod math**: numbers are **columns**, read **right-to-left**.
* Same block separation.
* Sum evaluated results.

---

## Status

✔️ Days 1 to 6 complete

Next step: Day 7

---

## Running Code

For each day:

```bash
python3 dayX_partY.py
```

Input files are expected to be named:

```
input.txt
```

---

## License

MIT
