from typing import List

from test_framework import generic_test

#h index is max val of h st the person has at least h papers each with at least h citations
def h_index(citations: List[int]) -> int:
    citations.sort()
    
    return 0


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
