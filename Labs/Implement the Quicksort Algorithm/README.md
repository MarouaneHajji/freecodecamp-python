# Quicksort Algorithm Implementation

## 📌 Overview

This project implements the **Quicksort algorithm**, a popular and efficient sorting algorithm based on the **divide-and-conquer** strategy.

The goal is to sort a list of integers from smallest to largest **without using built-in sorting functions**.

---

## ⚙️ How It Works

The algorithm follows these steps:

1. **Choose a Pivot**
   - The first element of the list is selected as the pivot.

2. **Partition the List**
   - Divide the list into three sublists:
     - Elements less than the pivot
     - Elements equal to the pivot
     - Elements greater than the pivot

3. **Recursive Sorting**
   - Apply the same process recursively to the "less" and "greater" sublists.

4. **Combine Results**
   - Concatenate the sorted sublists:
     ```
     sorted_list = sorted_less + equal + sorted_greater
     ```

---

## 🧠 Key Properties

- **Time Complexity:**
  - Average: O(n log n)
  - Worst: O(n²)

- **Space Complexity:**
  - O(n) due to new lists being created

- **Stable:**
  - This implementation is stable because it preserves duplicates properly.

---

## 🚫 Constraints

- No use of:
  - Built-in sorting methods (`sorted()`, `.sort()`)
  - External modules

- The original list must **not be modified**

---

## 🧪 Example Usage

```python
quick_sort([20, 3, 14, 1, 5])
# Output: [1, 3, 5, 14, 20]
quick_sort([87, 11, 23, 18, 18, 23, 11])
# Output: [11, 11, 18, 18, 23, 23, 87]
✅ Features
Handles empty lists
Works with duplicate values
Does not modify the original input list
Fully recursive implementation
📂 Project Structure
quicksort/
│
├── quicksort.py   # Main implementation
└── README.md      # Project documentation
🚀 Conclusion

This project demonstrates how the Quicksort algorithm works internally without relying on Python's built-in features, helping build a deeper understanding of recursion and algorithm design.