from typing import List
from test_framework import generic_test

#Bottom up soln O(n^2) time and O(1) space with input mutation
#n is the length of the last lvl
def minimum_path_weight(triangle: List[List[int]]) -> int:
    if not triangle:
        return 0
    for lvl in range(len(triangle)-2, -1, -1):
        for pos in range(len(triangle[lvl])-1, -1,-1):
            triangle[lvl][pos] = min(triangle[lvl+1][pos], triangle[lvl+1][pos+1]) + triangle[lvl][pos]
    return triangle[0][0]

# #Bottom up soln O(n^2) time and O(1) space with input mutation
# #n is the length of the last lvl
# def minimum_path_weight(triangle: List[List[int]]) -> int:
#     if not triangle:
#         return 0
#     prev = triangle[-1]
#     for lvl in range(len(triangle)-2, -1, -1):
#         cur = [0 for _ in range(len(triangle[lvl]))]
#         for pos in range(len(triangle[lvl])-1, -1,-1):
#             cur[pos] = min(prev[pos], prev[pos+1]) + triangle[lvl][pos]
#         prev = cur
#     return prev[0]

# #Time O(n^2) where n is the length of last lvl
# #Space is O(n^2) for the memo and call stack
# def minimum_path_weight(triangle: List[List[int]]) -> int:
#     if not triangle:
#         return 0
#     memo = {}
#     def recur(lvl, pos):
#         if (lvl, pos) in memo:
#             return memo[(lvl, pos)]
#         if pos >= lvl+1:
#             return inf
#         if lvl == len(triangle) -1:
#             return triangle[lvl][pos]
#         m = min(recur(lvl+1, pos), recur(lvl+1,pos+1)) + triangle[lvl][pos]
#         memo[(lvl,pos)] = m
#         return m
#     return recur(0,0)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
