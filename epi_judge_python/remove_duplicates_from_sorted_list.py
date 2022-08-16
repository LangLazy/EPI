from typing import Optional
from math import inf
from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    dummy = ListNode()
    dummy.data = -inf
    dummy.next = L
    head = L
    prev = dummy
    while head:
        if head.data == prev.data:
            prev.next = head.next
            head = head.next
        else:
            prev = head
            head = head.next
    return dummy.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
