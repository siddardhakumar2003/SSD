from dataclasses import dataclass
from typing import Optional
@dataclass
class Node:
    key: int
    height: int = 1
    left: Optional['Node'] = None
    right: Optional['Node'] = None


class BST:
    def __init__(self):
        self.root: Optional[Node] = None

    def insert(self, key: int):
        self.root = self._insert(self.root, key)

    def _insert(self, root: Optional[Node], key: int) -> Node:
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        return root

    def search(self, key: int) -> bool:
        return self._search(self.root, key)

    def _search(self, root: Optional[Node], key: int) -> bool:
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def get_height(self) -> int:
        return self._get_height(self.root)

    def _get_height(self, root: Optional[Node]) -> int:
        if root is None:
            return 0
        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)
        return 1 + max(left_height, right_height)

    def is_balanced(self) -> bool:
        return self._is_balanced(self.root)

    def _is_balanced(self, root: Optional[Node]) -> bool:
        if root is None:
            return True

        left_height = self._get_height(root.left)
        right_height = self._get_height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self._is_balanced(root.left) and self._is_balanced(root.right)


#AVL
class AVLTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def _get_node_height(self, node: Optional[Node]) -> int:
        return node.height if node else 0

    def _get_balance(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        return self._get_node_height(node.left) - self._get_node_height(node.right)

    def _right_rotate(self, y: Node) -> Node:
        x = y.left
        T2 = x.right if x else None

        # Rotate
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self._get_node_height(y.left), self._get_node_height(y.right))
        x.height = 1 + max(self._get_node_height(x.left), self._get_node_height(x.right))

        return x

    def _left_rotate(self, x: Node) -> Node:
        y = x.right
        T2 = y.left if y else None

        # Rotate
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self._get_node_height(x.left), self._get_node_height(x.right))
        y.height = 1 + max(self._get_node_height(y.left), self._get_node_height(y.right))

        return y

    def insert(self, key: int):
        self.root = self._insert(self.root, key)

    def _insert(self, root: Optional[Node], key: int) -> Node:
        # Standard BST insert
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            return root  # duplicates not allowed

        # Update height
        root.height = 1 + max(self._get_node_height(root.left),
                              self._get_node_height(root.right))

        # Get balance
        balance = self._get_balance(root)

        # Rebalance if needed
        # Left Left
        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)

        # Right Right
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)

        # Left Right
        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Right Left
        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def search(self, key: int) -> bool:
        return self._search(self.root, key)

    def _search(self, root: Optional[Node], key: int) -> bool:
        if root is None:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self._search(root.left, key)
        else:
            return self._search(root.right, key)

    def get_height(self) -> int:
        return self._get_node_height(self.root)

    def is_balanced(self) -> bool:
        return self._is_balanced(self.root)

    def _is_balanced(self, root: Optional[Node]) -> bool:
        if root is None:
            return True

        left_height = self._get_node_height(root.left)
        right_height = self._get_node_height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self._is_balanced(root.left) and self._is_balanced(root.right)

import time
if __name__ == "__main__":

    data_filename = "sorted_sensor_data.txt"
    target_filename = "search_target.txt"
    output_filename = "analysis.txt"
    #---Load Data--
    print(f"Loading data from {data_filename}...")
    keys_to_insert = []
    try:
        with open(data_filename, 'r') as f:
            for line in f:
                keys_to_insert.append(int(line.strip()))

        with open(target_filename, 'r') as f:
            search_key = int(f.read().strip())
        print(f"Data loaded. {len(keys_to_insert)} keys.")
        print(f"Search target: {search_key}")

    except FileNotFoundError:
        print(f"Error: Data files not found.")
        exit()

    import sys
    # We must increase Python’s recursion limit to allow the BST
    # to build its extremely deep, skewed tree (height = 50,000).
    # The default limit is ~1000.
    new_limit = len(keys_to_insert) + 10
    print(f"Setting recursion limit to {new_limit}...")
    sys.setrecursionlimit(new_limit)

    bst_tree = BST()
    avl_tree = AVLTree()

    #---Time BST Insertion--
    print("Inserting into BST...")
    bst_start_time = time.perf_counter()
    for key in keys_to_insert:
        bst_tree.insert(key)
    bst_end_time = time.perf_counter()
    bst_insert_time = bst_end_time- bst_start_time
    print(f"BST insertion time: {bst_insert_time:.6f}s")
    #---Time AVL Insertion--
    print("Inserting into AVL...")
    avl_start_time = time.perf_counter()
    for key in keys_to_insert:
        avl_tree.insert(key)
    avl_end_time = time.perf_counter()
    avl_insert_time = avl_end_time- avl_start_time
    print(f"AVL insertion time: {avl_insert_time:.6f}s")

    #---1. Get Tree Heights--
    bst_height = bst_tree.get_height()
    avl_height = avl_tree.get_height()

    #---2. Check Balance--
    bst_balanced = bst_tree.is_balanced()
    avl_balanced = avl_tree.is_balanced()

    #---3. Time Search--
    print(f"Searching for {search_key}...")

    # Time BST Search
    bst_search_start = time.perf_counter()
    bst_tree.search(search_key)
    bst_search_end = time.perf_counter()
    bst_search_time = bst_search_end- bst_search_start
    # Time AVL Search
    avl_search_start = time.perf_counter()
    avl_tree.search(search_key)
    avl_search_end = time.perf_counter()
    avl_search_time = avl_search_end- avl_search_start

    #---4. Calculate Ratio--
    # Handle division by zero just in case
    search_ratio = 0.0
    if avl_search_time > 0:
        search_ratio = bst_search_time / avl_search_time

    #---5. Write Report--
    print(f"Writing analysis to {output_filename}...")
    with open(output_filename, 'w') as report:
        report.write(f"BST_HEIGHT: {bst_height}\n")
        report.write(f"AVL_HEIGHT: {avl_height}\n")
        report.write(f"BST_IS_BALANCED: {bst_balanced}\n")
        report.write(f"AVL_IS_BALANCED: {avl_balanced}\n")
        report.write(f"BST_SEARCH_TIME: {bst_search_time}\n")
        report.write(f"AVL_SEARCH_TIME: {avl_search_time}\n")
        report.write(f"SEARCH_RATIO_BST_vs_AVL: {search_ratio}\n")
    print("Analysis complete.")