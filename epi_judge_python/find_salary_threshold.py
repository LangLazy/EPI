from functools import partial
from typing import List

from test_framework import generic_test

#what a great problemn time is O(nlogn) space is O(n)
def find_salary_cap(target_payroll: int, current_salaries: List[int]) -> float:
    current_salaries.sort()

    parition = len(current_salaries) #This index and on is the 2nd partition
    tot = sum(current_salaries)
    curSum = tot
    avg = target_payroll / len(current_salaries)
    partialSum = 0

    while curSum / len(current_salaries) >= avg and parition >= 0:
        parition -= 1
        partialSum += current_salaries[parition]
        curSum = tot - (partialSum - current_salaries[parition] * (len(current_salaries) - parition))
    parition += 1
    if parition > len(current_salaries):
        return -1.0 #The target payroll is larger than last years
    partialSum -= current_salaries[parition-1]
    return ((avg * len(current_salaries)) - (tot - partialSum))/(len(current_salaries) - parition)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('find_salary_threshold.py',
                                       'find_salary_threshold.tsv',
                                       find_salary_cap))
