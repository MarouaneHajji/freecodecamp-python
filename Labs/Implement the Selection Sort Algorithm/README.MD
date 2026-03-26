# Selection Sort Algorithm Implementation

## 📌 Overview

This project implements the **Selection Sort algorithm**, a simple and intuitive sorting algorithm.

Unlike some other sorting methods, Selection Sort works by repeatedly selecting the smallest element from the unsorted portion of the list and placing it in its correct position.

---

## ⚙️ How It Works

The algorithm follows these steps:

1. Start at the first index of the list.
2. Find the smallest element in the remaining unsorted portion.
3. Swap it with the current position (if needed).
4. Move to the next index and repeat.
5. Continue until the list is fully sorted.

---

## 🧠 Example Walkthrough

Given the list:


[33, 1, 89, 2]


Steps:

1. Find smallest → `1`, swap with `33`  
   → `[1, 33, 89, 2]`

2. Find smallest in remaining → `2`, swap with `33`  
   → `[1, 2, 89, 33]`

3. Find smallest → `33`, swap with `89`  
   → `[1, 2, 33, 89]`

---

## 🧠 Key Properties

- **Time Complexity:**
  - Best Case: O(n²)
  - Average Case: O(n²)
  - Worst Case: O(n²)

- **Space Complexity:**
  - O(1) (in-place sorting)

---

## 🚫 Constraints

- No use of:
  - `sorted()`
  - `.sort()`
  - External modules

- The list must be:
  - Modified **in-place**
  - Returned after sorting

- Avoid unnecessary swaps

---

## 🧪 Example Usage

```python
selection_sort([33, 1, 89, 2, 67, 245])
# Output: [1, 2, 33, 67, 89, 245]
selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3])
# Output: [3, 5, 12, 15, 16, 23, 72, 99, 567]
📂 Project Structure
selection-sort/
│
├── selection_sort.py   # Main implementation
└── README.md           # Documentation
🚀 Conclusion

This project demonstrates how Selection Sort works internally by manually selecting and placing elements in order. It helps build a strong understanding of algorithm fundamentals and in-place sorting.