from list_node import ListNode
from test_framework import generic_test


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    def reverse(head):
        cur = head
        past = None
        while cur:
            tmp = cur.next
            cur.next = past
            past = cur
            cur = tmp
        return past
    h1 = L
    h2 = L
    while h1 and h1.next:
        h1 = h1.next.next
        h2 = h2.next
    h1 = L
    h2 = reverse(h2)
    while h1 and h2:
        if h1.data != h2.data:
            return False
        h1 = h1.next
        h2 = h2.next
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
