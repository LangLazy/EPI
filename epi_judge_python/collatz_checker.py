from ast import main
from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    mainSet = set()
    def runCol(n):
        nonlocal mainSet
        if n in mainSet:
            return True
        curSet = set()
        while n != 1:
            curSet.add(n)
            mainSet.add(n)
            if n%2 == 0:
                n /= 2
            else:
                n = n*3 + 1
            if n in curSet:
                return False
            elif n in mainSet:
                return True
        return True
    for i in range(1,n+1):
        if not runCol(i):
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('collatz_checker.py',
                                       'collatz_checker.tsv',
                                       test_collatz_conjecture))
