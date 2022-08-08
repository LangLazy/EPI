from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    maxR = 0
    for i in range(len(A)):
        maxR = max(maxR-1, A[i])
        if i + maxR >= len(A) -1:
            return True
        if maxR == 0:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
