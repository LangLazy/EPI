from test_framework import generic_test


def look_and_say(n: int) -> str:
    def countOcur(s, pos) -> int:
        start = s[pos]
        while pos < len(s) and s[pos] == start:
            pos += 1
        return pos #the first diff spot
    def update(s) -> str:
        cur = 0
        ans = ""
        while cur < len(s):
            currentLet = s[cur]
            endPos = countOcur(s, cur)
            ans += str(endPos - cur)
            ans += currentLet
            cur = endPos
        return ans
    ans = "1"
    for i in range(n-1):
        ans = update(ans)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
