# Validate Binary Search Tree

Given the  `root`  of a binary tree,  _determine if it is a valid binary search tree (BST)_.

A  **valid BST**  is defined as follows:

-   The left subtree of a node contains only nodes with keys  **less than**  the node's key.
-   The right subtree of a node contains only nodes with keys  **greater than**  the node's key.
-   Both the left and right subtrees must also be binary search trees.

**Example 1:**

![example 1](../images/validatebstree1.jpg)

**Input:** root = [2,1,3]
**Output:** true

**Example 2:**

![example 2](../images/validatebstree2.jpg)

**Input:** root = [5,1,4,null,null,3,6]
**Output:** false
**Explanation:** The root node's value is 5 but its right child's value is 4.

**Constraints:**

-   The number of nodes in the tree is in the range  `[1, 104]`.
-   `-231  <= Node.val <= 231  - 1`

**Solution:**

- code: [validate_bstree.py](validate_bstree.py)
- test cases: [validate_bstree.py](../tests/validate_bstree.py)