from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    def recur(node, sum):
        if not node:
            return False
        if sum - node.data == 0 and node and not node.left and not node.right:
            return True
        return recur(node.left,sum - node.data ) or recur(node.right,sum - node.data )
    return recur(tree, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
