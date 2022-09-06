import heapq
from multiprocessing import heap
from typing import List

from test_framework import generic_test, test_utils

#Time O(klogk)
#Space O(k)
def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    toCheck = []
    heapq.heapify(toCheck)
    heapq.heappush(toCheck, (-A[0], 0))
    ans = []
    for _ in range(k):
        v = heapq.heappop(toCheck)
        ans.append(-v[0])
        l = 2*v[1]+1
        if l < len(A):
            heapq.heappush(toCheck, (-A[l], l))
        r = l+1
        if r < len(A):
            heapq.heappush(toCheck, (-A[r], r))
    return ans

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
