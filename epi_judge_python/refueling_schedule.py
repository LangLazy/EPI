import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

MPG = 20


# gallons[i] is the amount of gas in city i, and distances[i] is the
# distance city i to the next city.
#O(n) time and O(n) space
def find_ample_city(gallons: List[int], distances: List[int]) -> int:
    class ListNode:
        def __init__(self, id) -> None:
            self.id = id
            self.delta =  MPG*gallons[id] - distances[id]
            self.next = None
    head = ListNode(0)
    cur = head
    for i in range(1, len(gallons)):
        cur.next = ListNode(i)
        cur = cur.next
    cur.next = head
    length  = len(gallons)
    cur = head
    loopCount = 0
    while length != 1:
        if loopCount == length:
            break
        if cur.delta > 0:
            cur.delta = cur.delta + cur.next.delta
            if cur.next is head:
                head = cur
            cur.next = cur.next.next
            length -= 1
            loopCount = 0
        else:
            cur = cur.next
            loopCount += 1
    return head.id


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('refueling_schedule.py',
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
