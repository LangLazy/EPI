from typing import List

from test_framework import generic_test

#Time O(n^2) Space O(n)
def has_three_sum(A: List[int], t: int) -> bool:
    def twoSum(pos, num):
        lookup = set()
        for i in range(pos, len(A)):
            if A[i] in lookup or num == 2*A[i]:
                return True
            else:
                lookup.add(num - A[i])
        return False
    for x in range(len(A)):
        if twoSum(x, t - A[x]):
            return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
