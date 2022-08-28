import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if not tree:
        return []
    ans = []
    def recur(node, isLeft):
        if not node:
            return
        if isLeft or (not node.right and not node.left):
            ans.append(node)

        recur(node.left, isLeft)
        if isLeft and not node.left:
            recur(node.right, True)
        else:
            recur(node.right, False)

    def printRight(node):
        if not node:
            return
        elif not node.right and not node.left:
            return
        elif not node.right:
            printRight(node.left)
        else:
            printRight(node.right)
        ans.append(node)
    ans.append(tree)
    recur(tree.left, True)
    recur(tree.right, False)
    printRight(tree.right)
    return ans


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))