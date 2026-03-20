# Graphs & Trees Review

A structured reference covering graph types, traversals, representations, trees, tries, and heaps.

---

## Table of Contents

- [Graphs](#graphs)
  - [Graph Types](#graph-types)
  - [Graph Traversals](#graph-traversals)
  - [Graph Representations](#graph-representations)
- [Trees](#trees)
  - [Common Tree Types](#common-tree-types)
- [Tries (Prefix Trees)](#tries-prefix-trees)
- [Priority Queues & Heaps](#priority-queues--heaps)
  - [Heaps](#heaps)
  - [Python heapq Module](#python-heapq-module)

---

## Graphs

A **graph** is a set of **nodes (vertices)** connected by **edges**. Each node can connect to multiple others, forming a network.

**Common applications:** maps, social networks, recommendation systems, dependency resolution.

---

### Graph Types

| Type | Description |
|---|---|
| **Directed** | Edges have a direction (A → B); shown with arrows |
| **Undirected** | Edges have no direction; shown with plain lines |
| **Cyclic** | Contains at least one cycle (a path that starts and ends at the same node) |
| **Acyclic (DAG)** | No cycles — Directed Acyclic Graph |
| **Weighted** | Edges carry values (weights) used in calculations |
| **Edge Labeled** | Edges carry labels drawn next to them |
| **Disconnected** | Contains two or more nodes with no path between them |

---

### Graph Traversals

Visiting all nodes in a graph. The two main algorithms are:

#### Breadth-First Search (BFS)

- Uses a **queue**
- Explores nodes **level by level**
- Finds the **shortest path** in unweighted graphs

#### Depth-First Search (DFS)

- Uses a **stack** (or recursion)
- Explores a **branch fully** before backtracking
- Useful for **cycle detection** and pathfinding

| | BFS | DFS |
|---|---|---|
| **Data Structure** | Queue | Stack / Recursion |
| **Order** | Level by level | Branch by branch |
| **Best for** | Shortest path (unweighted) | Cycle detection, pathfinding |

---

### Graph Representations

#### Adjacency List

Each node stores a list of its neighbors.

- ✅ Space-efficient for **sparse** graphs
- ✅ Easy to iterate over neighbors

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"]
}
```

#### Adjacency Matrix

A 2D array where rows and columns represent nodes. A `1` at `[i][j]` means an edge exists between node `i` and node `j`.

- ✅ Fast to check if an edge exists between two nodes
- ❌ Space-intensive for large graphs

```python
#     A  B  C  D
matrix = [
    [0, 1, 1, 0],  # A
    [1, 0, 0, 1],  # B
    [1, 0, 0, 0],  # C
    [0, 1, 0, 0],  # D
]
```

---

## Trees

A **tree** is a special graph that is:
- **Acyclic** — no loops or cycles
- **Connected** — every node is reachable from every other node

---

### Common Tree Types

#### Binary Tree

Each node has **at most two children**: a left child and a right child.

```
        10
       /  \
      5    15
     / \
    3   7
```

#### Binary Search Tree (BST)

A binary tree with an ordering rule:
- **Left child** is always **less than** its parent
- **Right child** is always **greater than** its parent

This makes search, insert, and delete operations efficient at `O(log n)` on balanced trees.

---

## Tries (Prefix Trees)

A **trie** is a tree where each node represents a **character**. Used to store sets of strings efficiently.

- **Shared prefixes are stored only once** — saves memory
- Common use cases: **autocomplete**, **spell checking**

| Operation | Time Complexity |
|---|---|
| Search | `O(L)` where L = string length |
| Insert | `O(L)` where L = string length |

```
Words: ["car", "cat", "cart"]

root
 └── c
      └── a
           ├── r ✓
           │    └── t ✓
           └── t ✓
```

---

## Priority Queues & Heaps

### Priority Queues

An abstract data type where each element has a **priority**. Elements with higher priority are served first, regardless of insertion order.

| Structure | Order |
|---|---|
| Queue | FIFO — first inserted, first served |
| Stack | LIFO — last inserted, first served |
| Priority Queue | **Priority-based** — highest priority served first |

---

### Heaps

A specialized **tree-based** data structure that maintains the **heap property** between parent and child nodes.

#### Max-Heap

- Every parent is **≥** its children
- The **largest** element is always at the root

#### Min-Heap

- Every parent is **≤** its children
- The **smallest** element is always at the root

> Python's `heapq` module implements a **min-heap** by default.

---

### Python heapq Module

#### Basic Operations

```python
import heapq

my_heap = []

# Push elements
heapq.heappush(my_heap, 9)
heapq.heappush(my_heap, 3)
heapq.heappush(my_heap, 5)
print(my_heap)  # [3, 9, 5]

# Pop smallest element
print(heapq.heappop(my_heap))  # 3
print(my_heap)                 # [5, 9]

# Push + pop in one step
print(heapq.heappushpop(my_heap, 7))  # 5
print(my_heap)                        # [7, 9]

# Convert an existing list into a heap in-place
nums = [5, 7, 3, 1]
heapq.heapify(nums)  # [1, 7, 3, 5]
```

#### Using Priorities

Push tuples `(priority, value)` — the heap orders by the first element (lowest number = highest priority).

```python
my_heap = []
heapq.heappush(my_heap, (3, "A"))
heapq.heappush(my_heap, (2, "B"))
heapq.heappush(my_heap, (1, "C"))

print(heapq.heappop(my_heap))  # (1, "C") — highest priority
```

#### heapq Quick Reference

| Function | Description |
|---|---|
| `heappush(heap, item)` | Push item onto heap |
| `heappop(heap)` | Pop and return the smallest item |
| `heappushpop(heap, item)` | Push item, then pop and return the smallest |
| `heapify(list)` | Transform a list into a heap in-place |