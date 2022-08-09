def topDownCountScores(coins: list[int],amt: int, pos:int =0,memo={})->int:
    if (pos, amt) in memo:
        return memo[(pos, amt)]
    if amt == 0:
        return 1
    if pos >= len(coins) or amt < 0:
        return 0
    v = topDownCountScores(coins, amt - coins[pos], pos, memo) + topDownCountScores(coins, amt, pos+1, memo)
    memo[(pos,amt)] = v
    return v

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
c = [2,3,7]
print(bottomUp(12,c))