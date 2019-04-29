---
draft: True
revision: 1
template: base.html
title: TBD
tags: []
---

One single meta algorithm to solve all coding problems. 

One algorithm rules them all:
```
while problem is not solved:
    find tools in your toolbox that are applicable
    if no such tool:
        invent a new tool
```

Toolbox contains common data structures, algorithms, and techniques.
That means the better you memorize them, the faster you can solve a coding problem. In a bigger toolbox, the probability that you can find applicable tools are higher. This is still true even if your solving skills are excellent. If your toolbox is small, you'll spend more time to build intermediate tools, instead of solving one.

# Tools you should have in your toolbox
## Abstract Data Types
### Dictionary
- Abstract Implementation: BST
- Data Structure: leftMostChild rightSibling
- Operations: insert, lookup, delete
- Efficiency:
    - Worst: O(n)
    - Best: O(logn)
    - Average: O(logn)
    
### Priority Queue
- Abstract Implementation: Balanced Partially Ordered Tree
- Data Structure: Heap
- Operations: insert, deletemax
- Efficiency:
    - Worst: O(logn)

## Data Structures
### Linked list
- Representing a linked list using struct/class
```C++
    struct Node {
        int data,
        Node* next
    }
```
- Locating a node. Time complexity: O(n)
- Appending a node. Time complexity: O(1)
- Inserting a node. Time complexity: O(n)
- Deleting a node. Time complextiy: O(1)

### Tree
- Representing a tree
    - array of childs
    - leftmostchild and rightsibling
- Recursions in a tree
- How to evaluate a node
- preorder
- postorder

### Binary Tree
- Representing a binary tree
- inorder
- BST
    - lookup: O(logn)


### Binary Search Tree
### Priority Queue

## Techniques
- Recursion
- Divide to conquer

## Algorithms
### Sorting
#### Heap Sort
- Algorithm:
    - step 1: make a heap by continously apply insert to the heap (O(nlogn))
    - step 2: make a sorted array by continously apply deleteMax to the heap (O(nlogn))
