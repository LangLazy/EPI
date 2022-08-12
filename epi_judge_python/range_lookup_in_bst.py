import collections
from typing import List
from math import inf
from bst_node import BstNode
from test_framework import generic_test

Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
    ans = []
    def reportAll(node):
        if not node:
            return
        reportAll(node.left)
        ans.append(node.data)
        reportAll(node.right)
    def recur(tree, pivoted, left):
        if not tree:
            return
        if pivoted:
            if interval[0] <= tree.data and tree.data <= interval[1]:
                if left:
                    reportAll(tree.left)
                    ans.append(tree.data)
                    recur(tree.right, pivoted, left)
                else:
                    recur(tree.left, pivoted, left)
                    ans.append(tree.data)
                    reportAll(tree.right)
            elif tree.data < interval[0]:
                recur(tree.right, pivoted, left)
            else:
                recur(tree.left, pivoted,left)
        else:
            if interval[0] <= tree.data and tree.data <= interval[1]:
                recur(tree.left, True,False)
                ans.append(tree.data)
                recur(tree.right, True,True)
            elif tree.data < interval[0]:
                recur(tree.right, pivoted, left)
            else:
                recur(tree.left, pivoted,left)
    recur(tree, False, False)
    return ans
# def range_lookup_in_bst(tree: BstNode, interval: Interval) -> List[int]:
#     ans = []
#     def reportAll(node):
#         if not node:
#             return
#         reportAll(node.left)
#         ans.append(node.data)
#         reportAll(node.right)
#     def isIn(goal, has):
#         return goal[0] <= has[0] and has[1] <= goal[1]
#     def recur(node, goal, cur):
#         if not node:
#             return
#         if isIn(goal, cur):
#             reportAll(node)
#         elif node.data >= goal[0] and node.data <= goal[1]:
#             recur(node.left, goal, (cur[0], min(node.data, cur[1])))
#             ans.append(node.data)
#             recur(node.right, goal, (max(node.data, cur[0]),cur[1]))
#         elif node.data < goal[0]:
#             recur(node.right, goal, (max(node.data, cur[0]),cur[1]))
#         else:
#             recur(node.left, goal, (cur[0], min(node.data, cur[1])))
#     recur(tree, interval, (-inf,inf))
#     return ans


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('range_lookup_in_bst.py',
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
