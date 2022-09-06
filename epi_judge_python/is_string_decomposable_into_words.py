import functools
from typing import List, Set
from xml import dom

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

#A tabulation soln Time O((len(domains))^2Sum(len(w in dictionary))) Space O(len(str))
def decompose_into_dictionary_words(domain: str,
                                    dictionary: Set[str]) -> List[str]:
    dp = [-1 for  _ in range(len(domain)+1)]
    dp[-1] = 0
    for i in range(len(domain)-1, -1, -1):
        for w in dictionary:
            if domain.startswith(w, i) and i + len(w) <= len(domain) and dp[i+len(w)] != -1:
                dp[i] = i + len(w)
    if dp[0] == -1:
        return []
    else:
        ans = []
        curPos = 0
        while curPos < len(domain):
            ans.append(domain[curPos:dp[curPos]])
            curPos = dp[curPos]
        return ans

# #A memoized soln Time O((len(domains))^2Sum(len(w in dictionary))) Space O(len(str))
# def decompose_into_dictionary_words(domain: str,
#                                     dictionary: Set[str]) -> List[str]:
#     memo = set() #Stores if we have seen this pos and if it worked 
#     ans = []
#     def recur(pos: int) -> List[str]:
#         if pos >= len(domain):
#             return True
#         if pos in memo:
#             return False
#         for w in dictionary:
#             if domain.startswith(w, pos) and recur(pos + len(w)):
#                 ans.append(w)
#                 return True
#         memo.add(pos)
#         return False
#     recur(0)
#     ans.reverse()
#     return ans


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_decomposable_into_words.py',
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
