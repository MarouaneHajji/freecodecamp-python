### Visual Intuition

Imagine you are searching for √25:

- Start with a range: `[0, 25]`
- Take the middle → `12.5` → too big (since 12.5² > 25)
- New range: `[0, 12.5]`
- Take the middle again → `6.25` → still too big
- New range: `[0, 6.25]`
- Keep repeating...

Each step **cuts the search space in half**, getting closer and closer to the true answer.

---

## Algorithm Breakdown

1. **Input validation**
   - Reject negative numbers (no real square root)

2. **Handle trivial cases**
   - `√0 = 0`
   - `√1 = 1`

3. **Initialize bounds**
   ```python
   low = 0
   high = max(n, 1)
Iterate

Compute midpoint:

mid = (low + high) / 2

Check precision:

(high - low) / 2 <= tolerance
Decide which half to keep:
If mid² < n → move low up
Else → move high down
Stop when
Desired precision is reached ✅
OR max iterations exceeded ❌
Example Walkthrough

Let’s approximate:

square_root_bisection(9)

Steps (simplified):

Iteration	Low	High	Mid	Mid²	Action
1	0	9	4.5	20.25	Too big ↓
2	0	4.5	2.25	5.06	Too small ↑
3	2.25	4.5	3.375	11.39	Too big ↓
...	...	...	...	...	...

Eventually → ≈ 3.0

⏱️ Time Complexity
O(log(n / tolerance))

Why?

Each iteration halves the interval size
Faster convergence with higher tolerance
⚖️ Pros & Cons
✅ Advantages
Simple and reliable
Guaranteed convergence
Works for any continuous function
❌ Disadvantages
Slower than methods like Newton-Raphson
Requires an initial interval
💡 Key Insight

This method is essentially binary search applied to math.

Instead of searching in a list, you're searching in a range of real numbers.

🧪 Try It Yourself

Test with different values:

square_root_bisection(2)
square_root_bisection(0.25)
square_root_bisection(1000)

Try adjusting:

tolerance → for more/less precision
max_iterations → for performance limits
🏁 Conclusion

The Bisection Method is one of the most fundamental numerical algorithms.
It teaches you how to:

Think in terms of intervals
Approximate solutions iteratively
Balance precision and performance

Even though it's not the fastest method, it's one of the most robust and beginner-friendly ways to understand root-finding.

```
We want √81. The answer is somewhere between 0 and 81.

Iteration 1:  low=0,      high=81     → mid=40.5   → 40.5²=1640.25  (too big)  → high=40.5
Iteration 2:  low=0,      high=40.5   → mid=20.25  → 20.25²=410.06  (too big)  → high=20.25
Iteration 3:  low=0,      high=20.25  → mid=10.125 → 10.125²=102.5  (too big)  → high=10.125
Iteration 4:  low=0,      high=10.125 → mid=5.0625 → 5.0625²=25.6   (too small)→ low=5.0625
...
Converges → 9.0
```

Each iteration cuts the search space in half — this is why convergence is fast.

---

## Function Reference

### `square_root_bisection(square_target, tolerance=1e-7, max_iterations=100)`

Finds the square root of `square_target` using the bisection method.

#### Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `square_target` | `float` | *(required)* | The number to find the square root of |
| `tolerance` | `float` | `1e-7` | Acceptable margin of error (e.g. `0.0000001`) |
| `max_iterations` | `int` | `100` | Maximum number of halvings before giving up |

#### Return Value

| Condition | Returns | Prints |
|---|---|---|
| `square_target < 0` | raises `ValueError` | — |
| `square_target` is `0` or `1` | the number itself | `The square root of [n] is [n]` |
| Converges successfully | the approximate root | `The square root of [n] is approximately [root]` |
| Fails to converge | `None` | `Failed to converge within [max] iterations` |

#### Examples

```python
# Basic usage — default tolerance (1e-7) and max iterations (100)
square_root_bisection(81)
# Prints:  The square root of 81 is approximately 9.0
# Returns: 9.0

# Custom tolerance and iteration limit
square_root_bisection(225, 1e-5, 100)
# Prints:  The square root of 225 is approximately 15.000003...
# Returns: ~15.0

# Special cases
square_root_bisection(0)    # Prints: The square root of 0 is 0
square_root_bisection(1)    # Prints: The square root of 1 is 1

# Fractional input
square_root_bisection(0.25, 1e-7, 50)
# Prints:  The square root of 0.25 is approximately 0.5

# Not enough iterations to converge
square_root_bisection(225, 1e-7, 10)
# Prints:  Failed to converge within 10 iterations
# Returns: None

# Negative number
square_root_bisection(-4)
# Raises:  ValueError: Square root of negative number is not defined in real numbers
```

---

## How the Algorithm Works (Step by Step)

### 1. Input Validation

```python
if square_target < 0:
    raise ValueError('Square root of negative number is not defined in real numbers')
```

Square roots of negative numbers don't exist in real numbers, so the function rejects them immediately with a descriptive error.

### 2. Special Cases: 0 and 1

```python
if square_target in (0, 1):
    print(f'The square root of {square_target} is {square_target}')
    return square_target
```

Both 0 and 1 are their own square roots (`√0 = 0`, `√1 = 1`), so they are returned directly without any iteration.

### 3. Set the Initial Interval

```python
low = 0
high = max(square_target, 1)
```

The answer must lie somewhere between `0` and `max(square_target, 1)`.

**Why `max(square_target, 1)` and not just `square_target`?**
For numbers less than 1, the square root is actually *larger* than the number itself — for example, `√0.25 = 0.5`, and `0.5 > 0.25`. If `high` were set to `0.25`, the true answer `0.5` would fall outside the interval and the algorithm would never find it.

### 4. The Bisection Loop

```python
for _ in range(max_iterations):
    mid = (low + high) / 2

    if abs(mid * mid - square_target) <= tolerance:
        root = mid
        break

    if mid * mid < square_target:
        low = mid
    else:
        high = mid
```

Each iteration:
1. Computes the **midpoint** of the current interval
2. Checks if `mid²` is close enough to `square_target` (within `tolerance`)
3. If not, **discards the half** that cannot contain the answer and repeats

### 5. Convergence Check

```python
if root is None:
    print(f'Failed to converge within {max_iterations} iterations')
    return None

print(f'The square root of {square_target} is approximately {root}')
return root
```

If the loop finishes all iterations without satisfying the tolerance condition, the function reports failure and returns `None`.

---

## Complexity

| Property | Value |
|---|---|
| **Iterations needed** | `log₂(initial_interval / tolerance)` |
| **Time complexity** | O(log(n / tolerance)) |
| **Space complexity** | O(1) — no extra data structures used |

Because the interval is halved on every iteration, convergence is **logarithmically fast**. Finding `√225` to a tolerance of `1e-7` within an interval of `[0, 225]` requires at most `log₂(225 / 1e-7) ≈ 31` iterations.

---

## Tolerance vs. Iterations Trade-off

| Tolerance | Precision | Min iterations needed (for √225) |
|---|---|---|
| `1e-3` | ~3 decimal places | ~18 |
| `1e-5` | ~5 decimal places | ~25 |
| `1e-7` | ~7 decimal places | ~31 |

If `max_iterations` is set too low for the desired tolerance, the function will fail to converge and return `None`. Always ensure your iteration budget is at least `log₂(square_target / tolerance)`.

---

## File Structure

```
.
├── square_root_bisection.py   # Core implementation
└── README.md                  # This file
```

---

## Constraints

- **No imports allowed.** The entire implementation uses only built-in Python — no `math`, `numpy`, or any other module.
- Squaring is done as `mid * mid`, not with `**` or `math.pow`.