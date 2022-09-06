from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    po = 0
    ans = 0
    for i in range(len(col)-1,-1,-1):
        ans += (ord(col[i]) - ord('A') +1 ) * (26 ** po)
        po += 1
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
