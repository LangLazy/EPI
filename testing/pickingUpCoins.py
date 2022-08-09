memo = {}
coins = [20,5,20,20]
def recur(start, end):
    if end <= start:
        return 0
    if (start, end) in memo:
        return memo[(start, end)]
    m = coins[start]
    if coins[]
    m = max(coins[start] + min(recur(start+1,end-1), recur(start+2,end)), coins[end] + min(recur(start+1,end-1), recur(start,end-2)))
    memo[(start, end)] = m
    return m
print(recur(0, len(coins)-1))