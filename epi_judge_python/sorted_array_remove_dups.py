import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    toUse = 1
    for i in range(1,len(A),1):
        if A[toUse-1] == A[i]:
            continue
        else:
            A[toUse] = A[i]
            toUse += 1
    return toUse


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
