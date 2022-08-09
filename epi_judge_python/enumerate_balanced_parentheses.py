from typing import List

from test_framework import generic_test, test_utils

#Space O(s)
#Time O(n^2)
def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    memo = {}
    def recur(n):
        if n in memo:
            return memo[n][::1]
        if n == 0:
            return [""]
        ans = []
        for i in range(1,n+1):
            sub = ["(" + x + ")" for x in recur(i-1)]
            part = [x + y for x in sub for y in recur(n-i)]
            ans += part
        memo[n] = ans
        return ans
    return recur(num_pairs)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
