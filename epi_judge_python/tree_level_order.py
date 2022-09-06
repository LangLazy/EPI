from typing import List
from collections import deque
from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    q = deque([tree])
    ans = []
    while q:
        lvl = []
        v = len(q)
        for _ in range(v):
            cur = q.popleft()
            lvl.append(cur.data)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        ans.append(lvl)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
