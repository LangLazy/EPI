from operator import index
from typing import List
import heapq
from test_framework import generic_test
from collections import namedtuple

#Time O(sum lists * log k) where k is the number of lists
#Space O(k)
def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    indexPair = namedtuple('indexPair', ("element", "listNum"))
    q = []
    ix = [0 for _ in range(len(sorted_arrays))]
    heapq.heapify(q)
    ans = []

    for i in range(len(sorted_arrays)):
        if sorted_arrays[i]:
            heapq.heappush(q, indexPair(sorted_arrays[i][0], i))
            ix[i] += 1

    while q:
        cur = heapq.heappop(q)
        ans.append(cur.element)
        if ix[cur.listNum] >= len(sorted_arrays[cur.listNum]):
            continue
        heapq.heappush(q, indexPair(sorted_arrays[cur.listNum][ix[cur.listNum]],cur.listNum ))
        ix[cur.listNum] += 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
