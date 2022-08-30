from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    seen = {}
    startPos = 0
    maxLen = 0
    for pos, a in enumerate(A):
        if a in seen:
            if seen[a] >= startPos:
                startPos = seen[a] + 1
        seen[a] = pos
        maxLen = max(maxLen, pos - startPos + 1)
    return maxLen


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
