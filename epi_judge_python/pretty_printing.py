from typing import List
from math import inf
from test_framework import generic_test

#Bottom up DP
def minimum_messiness(words: List[str], line_length: int) -> int:
    dp = [inf for _ in range(len(words)+1)]
    dp[-1] = 0
    for i in range(len(words)-1,-1,-1):
        currentLength = len(words[i])
        currentPos = i
        while currentLength <= line_length:
                dp[i] = min(dp[i], dp[currentPos +1 ] + (line_length-currentLength)**2)
                currentPos += 1
                if currentPos >= len(words):
                    break
                currentLength +=  1 +len(words[currentPos])
                pass
    return dp[0]

#time O(n^2) space O(n)
# def minimum_messiness(words: List[str], line_length: int) -> int:
#     memo ={}
#     def recur(pos):
#         if pos in memo:
#             return memo[pos]
#         if pos >= len(words):
#             return 0
#         currentLength = len(words[pos])
#         currentPos = pos
#         minBadness = inf
#         while currentLength <= line_length:
#             minBadness = min(minBadness, recur(currentPos+1) + (line_length-currentLength)**2)
#             currentPos += 1
#             if currentPos >= len(words):
#                 break
#             currentLength += len(words[currentPos]) + 1
#         memo[pos] = minBadness
#         return minBadness
#     return recur(0)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pretty_printing.py',
                                       'pretty_printing.tsv',
                                       minimum_messiness))
