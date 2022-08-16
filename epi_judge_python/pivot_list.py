import functools
from typing import List, Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    head = ListNode()
    small = head
    largeHead = ListNode()
    large = largeHead
    eqHead = ListNode()
    eq = eqHead
    cur = l
    while cur:
        tmp = cur.next
        cur.next = None
        if cur.data < x:
            small.next = cur
            small = small.next
        elif cur.data > x:
            large.next = cur
            large = large.next
        else:
            eq.next = cur
            eq = eq.next
        cur = tmp
    if eqHead.next:
        small.next = eqHead.next
        eq.next = largeHead.next
    else:
        small.next =  largeHead.next
    return head.next


def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
