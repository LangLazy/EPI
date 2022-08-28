from test_framework import generic_test

#Time and space O(ab)
# def levenshtein_distance(A: str, B: str) -> int:
#     memo = {}
#     def recur(apos, bpos):
#         if (apos, bpos) in memo:
#             return memo[(apos, bpos)]
#         if apos >= len(A):
#             return len(B) - bpos
#         elif bpos >= len(B):
#             return len(A) - apos       
#         elif A[apos] == B[bpos]:
#             return recur(apos+1, bpos+1)
#         else:
#             v= min(recur(apos+1, bpos+1),recur(apos, bpos+1),recur(apos+1, bpos)) +1
#             memo[(apos, bpos)] = v
#             return v
#     return recur(0,0)

#Time and space O(ab)
# def levenshtein_distance(A: str, B: str) -> int:
#     dp = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
#     for apos in range(len(A),-1,-1):
#         for bpos in range(len(B),-1,-1):
#             if apos == len(A):
#                 dp[apos][bpos] = len(B) - bpos
#             elif bpos == len(B):
#                 dp[apos][bpos] = len(A) - apos
#             elif A[apos] == B[bpos]:
#                 dp[apos][bpos] = dp[apos+1][bpos+1]
#             else:
#                 dp[apos][bpos] = min(dp[apos+1][bpos+1], dp[apos+1][bpos], dp[apos][bpos+1])+1
#     return dp[0][0]
#Time O(ab) Space O(min(a,b))
def levenshtein_distance(A: str, B: str) -> int:
    sm,la = A,B
    if len(A) > len(B):
        sm,la = la,sm
    cur = [0 for _ in range(len(sm)+1)]
    prev = [0 for _ in range(len(sm)+1)]
    for lapos in range(len(la),-1,-1):
        for smpos in range(len(sm),-1,-1):
            if lapos == len(la):
                cur[smpos] = len(sm) - smpos
            elif smpos == len(sm):
                cur[smpos] = len(la) - lapos
            elif sm[smpos] == la[lapos]:
                cur[smpos] = prev[smpos+1]
            else:
                cur[smpos] = min(prev[smpos+1],  prev[smpos], cur[smpos+1])+1
        prev = cur
        cur =   [0 for _ in range(len(sm)+1)]
    return prev[0]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('levenshtein_distance.py',
                                       'levenshtein_distance.tsv',
                                       levenshtein_distance))
