from collections import deque
from math import inf
import queue
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    q = deque([(tree, -inf, inf)])
    while q:
        tree, start, stop = q.popleft()
        if start <= tree.data <= stop:
            if tree.right:
                q.append((tree.right, tree.data, stop))
            if tree.left:
                q.append((tree.left, start, tree.data))
        else:
            return False
    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
