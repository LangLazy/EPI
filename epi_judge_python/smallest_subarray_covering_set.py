from math import inf
import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    seen = {}
    minS = 0
    minE = inf
    uCount = 0
    end = 0
    for i in range(len(paragraph)):
        while uCount < len(keywords) and end < len(paragraph):
            if paragraph[end] in seen:
                seen[paragraph[end]] += 1
            elif paragraph[end] in keywords:
                seen[paragraph[end]] = 1
                uCount += 1
            end += 1
        if uCount != len(keywords):
            break
        else:
            if end - i < minE - minS:
                minS, minE = i, end
            if paragraph[i] in seen:
                if seen[paragraph[i]] == 1:
                    del seen[paragraph[i]]
                    uCount -= 1
                else:
                    seen[paragraph[i]] -= 1
    return Subarray(minS, minE-1)


@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
