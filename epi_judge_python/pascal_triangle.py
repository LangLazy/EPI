from typing import List

from test_framework import generic_test


def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []
    ans = [[1]]
    for lvl in range(1, n):
        cur = []
        for k in range(lvl+1):
            entry = 0
            if k - 1 >= 0 :
                entry += ans[lvl-1][k-1]
            if k < len(ans[lvl-1]):
                entry += ans[lvl-1][k]
            cur.append(entry)
        ans.append(cur)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
