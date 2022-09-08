from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L
    oddH = ListNode()
    odd = oddH
    cur = L
    past = None
    while cur and cur.next:
        onode = cur.next
        odd.next = onode
        odd = onode
        cur.next = cur.next.next
        past = cur
        cur = cur.next
        onode.next = None
    if cur and not cur.next:
        cur.next = oddH.next
    else:
        past.next = oddH.next
    return L


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
