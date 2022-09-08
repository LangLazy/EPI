from typing import Iterator, List
import heapq
from test_framework import generic_test


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    heap = []
    count = 0
    ans = []
    while count < k and sequence:
        heapq.heappush(heap, next(sequence))
        count += 1
    for num in sequence:
        ans.append(heapq.heappop(heap))
        heapq.heappush(heap, num)
    while heap:
        ans.append(heapq.heappop(heap))
    return ans


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
