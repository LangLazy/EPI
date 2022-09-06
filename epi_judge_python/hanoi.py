import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3

#Recursion is magic!
def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def recur(n, start, unused, end)-> List[List[int]]:
        if n == 0:
            return []
        elif n == 1:
            return [[start, end]]
        else:
            partial = recur(n-1, start, end, unused)
            partial += [[start, end]]
            partial += recur(n-1, unused, start, end)
            return partial
    return recur(num_rings, 0,2,1)
    # def recur(n, start, end) -> List[List[int]]:
    #     if n == 0:
    #         return
    #     elif n == 1:
    #         return [[start, end]]
    #     else:
    #         unused = 0
    #         if start != 1 and end != 1:
    #             unused = 1
    #         elif start !=2 and end != 2:
    #             unused = 2
    #         curAns = recur(n-1, start, unused)
    #         curAns.append([start, end])
    #         for i in range(1, n-1):
    #             pans = recur(n-i-1, unused, start)
    #             curAns += pans
    #             curAns.append([unused, end])
    #             unused, start = start, unused
    #         curAns.append([unused, end])
    #         return curAns
    # return recur(num_rings, 0, 1)


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
