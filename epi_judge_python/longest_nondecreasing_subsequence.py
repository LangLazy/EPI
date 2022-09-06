from typing import List

from test_framework import generic_test

def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
    dp = [1 for _ in range(len(A))]
    maxV = 0
    for i in range(len(A)-1,-1,-1):
        for k in range(i+1, len(A)):
            if A[k] >= A[i]:
                dp[i] = max(dp[i], 1 + dp[k])
        maxV = max(maxV, dp[i])
    return maxV


# def longest_nondecreasing_subsequence_length(A: List[int]) -> int:
#     if not A:
#         return 0
#     memo = {}
#     def recur(pos):
#         if pos >= len(A):
#             return 0
#         elif pos in memo:
#             return memo[pos]
#         maxV = 1
#         for i in range(pos+1,len(A)):
#             if A[i] >= A[pos]:
#                 maxV = max(maxV, 1 + recur(i))
#         memo[pos] = maxV
#         return maxV
#     maxV = 1
#     for i in range(len(A)):
#         maxV = max(maxV, recur(i))
#     return maxV


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_nondecreasing_subsequence.py',
            'longest_nondecreasing_subsequence.tsv',
            longest_nondecreasing_subsequence_length))
