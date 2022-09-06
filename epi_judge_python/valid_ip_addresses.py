from typing import List

from test_framework import generic_test


def get_valid_ip_address(s: str) -> List[str]:
    if len(s) > 12 or len(s)<4:
        return []
    ans = []
    for p1 in range(3):
        l1 = s[:p1+1]
        if (len(l1) > 1 and l1[0] == '0') or int(l1) > 255:
            continue
        for p2 in range(p1+1, p1 +4):
            if p2 >= len(s):
                continue
            l2 = s[p1+1:p2+1]
            if (len(l2) > 1 and l2[0] == '0') or int(l2) > 255:
                continue
            for p3 in range(p2+1, p2+4):
                if p3 >= len(s):
                    continue
                l3 =  s[p2+1:p3+1]
                if (len(l3) > 1 and l3[0] == '0') or int(l3) > 255:
                    continue
                for p4 in range(p3+1, p3+4):
                    if p4 == len(s) -1:
                        l4 =  s[p3+1:]
                        if (len(l4) > 1 and l4[0] == '0') or int(l4) > 255:
                            continue
                        ans.append(l1 +"." + l2 + "." + l3 + "." + l4)

    return ans


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('valid_ip_addresses.py',
                                       'valid_ip_addresses.tsv',
                                       get_valid_ip_address,
                                       comparator=comp))
