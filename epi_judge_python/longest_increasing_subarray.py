import collections
from typing import List
from test_framework import generic_test

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_longest_increasing_subarray(A: List[int]) -> Subarray:
    start = 0
    end = 0
    mStart = 0
    mEnd = 0
    for i in range(1, len(A)):
        if A[i] <= A[i-1]:
            start = i
        end = i
        if end - start >  mEnd - mStart:
            mStart, mEnd = start, end
    return Subarray(mStart, mEnd)


def find_longest_increasing_subarray_wrapper(A):
    result = find_longest_increasing_subarray(A)
    return result.end - result.start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_increasing_subarray.py',
            'longest_increasing_subarray.tsv',
            find_longest_increasing_subarray_wrapper))
