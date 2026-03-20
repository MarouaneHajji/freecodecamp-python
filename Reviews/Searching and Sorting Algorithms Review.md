# Searching & Sorting Algorithms Review

A structured reference covering linear search, binary search, divide-and-conquer, and merge sort.

---

## Table of Contents

- [Searching Algorithms](#searching-algorithms)
  - [Linear Search](#linear-search)
  - [Binary Search](#binary-search)
  - [Linear vs Binary Search](#linear-vs-binary-search)
- [Sorting Algorithms & Divide-and-Conquer](#sorting-algorithms--divide-and-conquer)
  - [Merge Sort](#merge-sort)

---

## Searching Algorithms

Searching algorithms locate a target value within a list and return its index, or `-1` if not found.

---

### Linear Search

Iterates through the list item by item from the beginning until the target is found.

- Returns the **index** of the target if found
- Returns **`-1`** if the target is not in the list
- Not efficient for large lists — checks every element in the worst case

| Complexity | Value |
|---|---|
| Time | `O(n)` — grows linearly with list size |
| Space | `O(1)` — no additional memory needed |

```python
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
```

---

### Binary Search

Repeatedly divides the list in half, checking whether the target is in the left or right half, until it is found or the search space is exhausted.

> ⚠️ **Requirement:** the list must be **sorted** (ascending or descending) before applying binary search.

**How it works:**
1. Check the middle element
2. If it matches the target → return its index
3. If the target is smaller → search the **left** half
4. If the target is larger → search the **right** half
5. Repeat until found, or return `-1` if not found

| Complexity | Value |
|---|---|
| Time | `O(log n)` — grows logarithmically with list size |
| Space | `O(1)` — no additional memory needed |

```python
def binary_search(lst, target):
    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

---

### Linear vs Binary Search

| | Linear Search | Binary Search |
|---|---|---|
| **Requirement** | None | List must be sorted |
| **Time Complexity** | `O(n)` | `O(log n)` |
| **Space Complexity** | `O(1)` | `O(1)` |
| **Best for** | Small or unsorted lists | Large sorted lists |
| **Efficiency** | Slower on large data | Much faster on large data |

---

## Sorting Algorithms & Divide-and-Conquer

**Divide-and-Conquer** is a technique that breaks a problem into smaller sub-problems, solves each one, then combines the results. It commonly relies on **recursion** and underpins many efficient sorting algorithms.

---

### Merge Sort

A sorting algorithm that applies divide-and-conquer by recursively splitting a list into halves, then merging them back together in sorted order.

**How it works:**
1. **Divide** — recursively split the list in half until each sub-list has one element
2. **Conquer** — a single element is trivially sorted
3. **Merge** — repeatedly merge adjacent sub-lists back together in sorted order

```python
def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

| Complexity | Value | Reason |
|---|---|---|
| Time | `O(n log n)` | List is halved `log n` times, each merge takes `O(n)` |
| Space | `O(n)` | Not in-place — requires extra memory for sub-lists |