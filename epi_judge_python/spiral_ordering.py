from typing import List

from test_framework import generic_test

#This does a spiral rectangular matrix

# ans = []
#         if not square_matrix:
#             return ans
#         def printShell(inWards: int):
#             hspan = len(square_matrix) - 2*inWards
#             vspan = len(square_matrix[0]) - 2*inWards
#             for v in range(vspan):
#                 ans.append(square_matrix[inWards][inWards+v])
#             for h in range(1,hspan):
#                 ans.append(square_matrix[inWards+h][inWards+vspan-1])
#             if hspan != 1:
#                 for v in range(1,vspan):
#                     ans.append(square_matrix[inWards+hspan-1][inWards+vspan-1 -v])
#             if vspan != 1:
#                 for h in range(1,hspan-1):
#                     ans.append(square_matrix[inWards+hspan-1-h][inWards])
#         for i in range(((min(len(square_matrix), len(square_matrix[0]))+1)//2)):
#             printShell(i)
#         return ans



def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    ans = []
    if not square_matrix:
        return ans
    def printShell(inWards: int):
        hspan = len(square_matrix) - 2*inWards
        vspan = len(square_matrix[0]) - 2*inWards
        for v in range(vspan):
            ans.append(square_matrix[inWards][inWards+v])
        for h in range(1,hspan):
            ans.append(square_matrix[inWards+h][inWards+vspan-1])
        for v in range(1,vspan):
            ans.append(square_matrix[inWards+hspan-1][inWards+vspan-1 -v])
        for h in range(1,hspan-1):
            ans.append(square_matrix[inWards+hspan-1-h][inWards])
    for i in range(((min(len(square_matrix), len(square_matrix[0]))+1)//2)):
        printShell(i)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
