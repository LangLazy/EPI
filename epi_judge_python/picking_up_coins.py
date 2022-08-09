from typing import List

from test_framework import generic_test

#This problem is so awful
#The book says only even length lists but it tests on odd?
#It says nothing about the other player trying to minimize you, it just says max profit you can get if you move first?w
#Key insight is that if the other player is maximizing them they want the worst for you so you have to pick the worst of the 4 possible reccursive casesw
def maximum_revenue(coins: List[int]) -> int:
    memo = {}
    def recur(start, end):
        if end < start:
            return 0
        if (start, end) in memo:
            return memo[(start, end)]
        m = max(coins[start] + min(recur(start+1,end-1), recur(start+2,end)), coins[end] + min(recur(start+1,end-1), recur(start,end-2)))
        memo[(start, end)] = m
        return m
    return recur(0, len(coins)-1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
