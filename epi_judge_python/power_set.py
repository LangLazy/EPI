from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    if not input_set:
        return [[]]
    ans = [[]]
    for i in range(len(input_set)):
        for x in range(len(ans)):
            ans.append(ans[x].copy())
            ans[-1].append(input_set[i])
    return ans
    # def recur(pos):
    #     if pos == len(input_set):
    #         return [[]]
    #     else:
    #         prev = recur(pos+1)
    #         for i in range(len(prev)):
    #             prev.append(prev[i].copy())
    #             prev[-1].append(input_set[pos])
    #         return prev
    # return recur(0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
