import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    def cycLen(l):
        fast, slow = l, l
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break
        if not (fast and fast.next): #No Loop
            counter = 0
            while l:
                counter += 1
                l = l.next
            return (counter,0)
        else: #Has Loop
            slow = l
            count = 0
            while slow is not fast:
                count += 1
                slow = slow.next
                fast = fast.next
            slow = slow.next
            cycle = 1
            while slow is not fast:
                slow = slow.next
                cycle +=1
            return (count, cycle)
    p0 = cycLen(l0)
    p1 = cycLen(l1)
    if p0[1] != p1[1]:
        return None
    c0 = l0
    c1 = l1
    if p0[0] < p1[0]:
        l0,l1 = l1,l0
        p0,p1 = p1,p0
        c0,c1 = c1,c0
    for _ in range(p0[0]-p1[0]):
        c0 = c0.next
    for _ in range(p1[0]):
        if c0 is c1:
            return c0
        c0,c1 = c0.next, c1.next
    for _ in range(p0[1]):
        if c1 is c0:
            return c0
        c1 = c1.next
    return None


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
