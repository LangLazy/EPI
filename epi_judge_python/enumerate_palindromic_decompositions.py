from typing import List

from test_framework import generic_test

#n2^n worst case lol
def palindrome_decompositions(text: str) -> List[List[str]]:
    memo = {}
    def recur(pos):
        if pos in memo:
            return memo[pos][::1]
        if pos >= len(text):
            return []
        ans = []
        for i in range(pos, len(text),1):
            if isPalindrome(pos, i):
                p1 = text[pos:i+1]
                part = recur(i+1)
                if len(part) == 0:
                    ans += [[p1]]
                else:
                    ans += [[p1] + x for x in part]
        memo[pos] = ans
        return ans
    def isPalindrome(start, end):
        while start <= end:
            if text[start] != text[end]:
                return False
            start, end = start+1, end-1
        return True
    return recur(0)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
