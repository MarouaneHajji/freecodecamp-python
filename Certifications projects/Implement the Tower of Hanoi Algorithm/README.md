# Tower of Hanoi — Python Solution

## Overview

The **Tower of Hanoi** is a classic mathematical puzzle invented by the French mathematician Édouard Lucas in 1883. This project provides a clean, recursive Python solution that solves the puzzle for any positive number of disks and returns a full log of every move taken.

---

## The Puzzle

### Setup

The puzzle consists of **three rods** and **n disks** of distinct sizes. At the start, all disks are stacked on the first rod in decreasing order — the largest disk at the bottom and the smallest on top.

```
Rod A        Rod B        Rod C
 [1]          [ ]          [ ]
 [2]
 [3]
```

### Goal

Move the entire stack from the **first rod** to the **last rod**, preserving the same descending order.

### Rules

1. You may move **only one disk at a time**.
2. You may only move the **top-most disk** on any rod.
3. You **cannot place a larger disk on top of a smaller one**.

---

## How the Algorithm Works

The solution uses **recursion** — the most natural fit for this problem. The key insight is:

> To move `n` disks from a source rod to a target rod, you can always break the problem into three smaller steps.

### Recursive Strategy

Given three rods — **source**, **target**, and **auxiliary**:

1. **Move the top `n-1` disks** from `source` → `auxiliary` (using `target` as buffer).
2. **Move the largest disk** (now exposed) from `source` → `target`.
3. **Move the `n-1` disks** from `auxiliary` → `target` (using `source` as buffer).

Steps 1 and 3 are the same problem with a smaller `n`, so they call themselves recursively. The recursion bottoms out when `n = 0` (nothing to move).

### Visual Walkthrough (n = 3)

```
Step 0: [3, 2, 1] [] []       ← initial state
Step 1: [3, 2] [] [1]         ← disk 1 → rod C
Step 2: [3] [2] [1]           ← disk 2 → rod B
Step 3: [3] [2, 1] []         ← disk 1 → rod B
Step 4: [] [2, 1] [3]         ← disk 3 → rod C
Step 5: [1] [2] [3]           ← disk 1 → rod A
Step 6: [1] [] [3, 2]         ← disk 2 → rod C
Step 7: [] [] [3, 2, 1]       ← disk 1 → rod C ✓
```

---

## Complexity

| Property | Value |
|---|---|
| **Number of moves** | 2ⁿ − 1 |
| **Time complexity** | O(2ⁿ) |
| **Space complexity** | O(n) — recursion call stack depth |

For example:
- 3 disks → 7 moves
- 4 disks → 15 moves
- 10 disks → 1,023 moves
- 20 disks → 1,048,575 moves

---

## Function Reference

### `hanoi_solver(n)`

Solves the Tower of Hanoi puzzle for `n` disks.

**Parameter**

| Name | Type | Description |
|---|---|---|
| `n` | `int` | Total number of disks (must be a positive integer) |

**Returns**

A `str` containing the board state after every move, including the initial arrangement. Each line represents one state in the format:

```
[rod_A] [rod_B] [rod_C]
```

Disks are represented as integers (smallest = `1`, largest = `n`). Each rod is shown as a Python list, with the rightmost element being the top of the stack.

**Example**

```python
print(hanoi_solver(2))
```

```
[2, 1] [] []
[2] [1] []
[] [1] [2]
[] [] [2, 1]
```

---

## Internal Design

### Data Structure

The three rods are stored as a list of three Python lists:

```python
rods = [list(range(n, 0, -1)), [], []]
# e.g. for n=3: [[3, 2, 1], [], []]
```

The **end of each list** represents the **top of the rod**. Moving a disk uses `pop()` (remove top) and `append()` (place on top), keeping all operations O(1).

### State Snapshot

After every single-disk move, the helper `state()` is called:

```python
def state():
    return ' '.join(str(rod) for rod in rods)
```

This converts each rod list to its string representation and joins them with spaces — producing output like `[3, 2] [] [1]`.

### Move Counting

The function records the initial state plus one state per move, giving a total of **2ⁿ lines** in the output (initial + 2ⁿ − 1 moves).

---

## Usage

```python
# Solve for 3 disks
result = hanoi_solver(3)
print(result)

# Count the number of moves (subtract 1 for the initial state)
moves = result.strip().split('\n')
print(f"Solved in {len(moves) - 1} moves")  # → Solved in 7 moves
```

---

## File Structure

```
.
├── hanoi_solver.py   # Core algorithm with inline comments
└── README.md         # This file
```

---

## Background

The Tower of Hanoi problem has a well-known connection to **binary numbers** and **Gray codes** — each move corresponds to flipping the lowest set bit, and the sequence of states traces a Gray code path. It also appears in discussions of **recursive thinking**, **divide and conquer**, and **exponential complexity** in computer science courses worldwide.