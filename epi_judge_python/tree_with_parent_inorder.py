from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    past = None
    cur = tree
    ans = []
    goneUp = False
    while cur:
        if goneUp:
            if past == cur.right :
                past = cur
                cur = cur.parent
                goneUp = True
            elif not cur.right:
                ans.append(cur.data)
                past = cur
                cur = cur.parent
                goneUp = True
            else:
                goneUp = False
                ans.append(cur.data)
                cur = cur.right
        else:
            if cur.left:
                cur = cur.left
                continue
            else:
                ans.append(cur.data)
                if cur.right:
                    cur = cur.right
                else:
                    goneUp = True
                    past = cur
                    cur = cur.parent
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
