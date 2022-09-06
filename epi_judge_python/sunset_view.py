from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    #Sorted in dec order
    ans = []
    def binSearch(num):
        l,r = 0, len(ans)
        while l <= r:
            mid = l +(r-l)//2
            if num < ans[mid][0]:
                l = mid + 1 
            else:
                r = mid - 1
        return l
    for pos, s in enumerate(sequence):
        if not ans:
            ans.append((s,pos))
            continue
        if s >= ans[-1][0]:
            v = binSearch(s)
            ans = ans[:v]
            ans.append((s,pos))
            pass
        else:
            ans.append((s,pos))
    return [p for _,p in ans][::-1]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
