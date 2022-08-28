from typing import List

from test_framework import generic_test


def longest_contained_range(A: List[int]) -> int:
    s = set()
    for a in A:
        s.add(a)
    maxV = 0
    for k in s:
        if k - 1 in s:
            continue
        else:
            cur = k
            while cur in s:
                cur += 1
            maxV = max(maxV, cur - k)
    return maxV


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('longest_contained_interval.py',
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))
