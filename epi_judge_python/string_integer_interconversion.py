import math
from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    ans = []
    if x < 0:
        ans.append('-')
        x *= -1
    elif x == 0:
        return "0"
    dec = math.floor(math.log(x,10))
    curPlace = 10 ** dec
    while curPlace >=1:
        v = x//curPlace
        ans.append(chr(ord('0') + v))
        x -= v * curPlace
        curPlace = curPlace // 10
    return ''.join(ans)


def string_to_int(s: str) -> int:
    end = -1
    mutl = 1
    if s[0] == '-':
        end = 0
        mutl = -1
    elif s[0] == '+':
        end = 0
    pow = 0
    cur = 0
    for i in range(len(s)-1,end,-1):
        cur += (ord(s[i]) - ord('0'))*(10 **pow)
        pow += 1
    return cur * mutl


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
