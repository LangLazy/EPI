from typing import List

from test_framework import generic_test

#Watch out for default param dicts lol
def num_combinations_for_final_score(amt: int ,coins: list[int]) -> int:
    #Time O(amt*len(coins))
    #Space O(amt)
    def topDown(amt: int ,coins: list[int],memo, pos:int) -> int:
        if (pos, amt) in memo:
            return memo[(pos,amt)]
        if amt == 0:
            return 1
        if pos >= len(coins) or amt < 0:
            return 0
        v =  topDown(amt - coins[pos], coins,memo, pos) + topDown(amt, coins, memo, pos+1)
        memo[(pos, amt)] = v
        return v
    #Time O(amt*len(coins))
    #Space O(amt)
    def bottomUp(amt: int ,coins: list[int]) -> int:
        cur = [0 for _ in range(amt+1)]
        cur[0] = 1
        prev = [0 for _ in range(amt+1)]
        #dp[i][j] is the number of ways to make j from coins up to pos i
        for h in range(len(coins)):
            for v in range(1,amt+1,1):
                if h > 0:
                    cur[v] += prev[v] 
                if v - coins[h] >= 0:
                    cur[v] += cur[v - coins[h]]
            prev = cur
            cur = [0 for _ in range(amt+1)]
            cur[0] = 1
        return prev[-1]  

    return bottomUp(amt ,coins)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
