from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    def rotateLayer(offset:int):
        len(square_matrix) - 2*offset - 1
        for i in range(len(square_matrix) - 2*offset - 1):
            a = square_matrix[offset][offset + i]
            b = square_matrix[offset+i][len(square_matrix) - offset -1 ]
            c = square_matrix[len(square_matrix) - offset -1][len(square_matrix) - offset -1-i]
            d = square_matrix[len(square_matrix) - offset -1 - i][offset]
            square_matrix[offset][offset + i] = d
            square_matrix[offset+i][len(square_matrix) - offset -1 ] = a
            square_matrix[len(square_matrix) - offset -1][len(square_matrix) - offset -1-i] = b
            square_matrix[len(square_matrix) - offset -1 - i][offset] = c
    for i in range((len(square_matrix)+1)//2):
        rotateLayer(i)
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
