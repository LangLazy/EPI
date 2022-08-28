from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s: str) -> str:
    def readNum(pos):
        end = pos #The first non digit
        while s[end].isdigit():
            end += 1
        cur = 0
        po = 0
        for i in range(end-1,pos-1,-1):
            cur += int(s[i]) * (10 ** po)
            po += 1
        return (cur, end)
    pos = 0
    ans = []
    while pos < len(s):
        num, pos = readNum(pos)
        for _ in range(num):
            ans.append(s[pos])
        pos += 1
    b = "".join(ans)
    print(type(b))
    return "ooooooo"


def encoding(s: str) -> str:
    if not s:
        return ""
    ans = []
    curChar = s[0]
    curCount = 1
    for i in range(1,len(s)+1):
        if i == len(s) or s[i] != curChar:
            ans.append(str(curCount))
            ans.append(curChar)
        if s[i] != curChar:
            curChar = s[i]
            curCount = 1
        elif s[i] == curChar:
            curCount += 1
    p = ''.join(ans)
    return p


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
