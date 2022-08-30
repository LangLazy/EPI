from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    map = {
        '1': ['1'],
        '0': ['0'],
        '2': ['A','B','C'],
        '3': ['D','E','F'],
        '4': ['G','H','I'],
        '5': ['J','K','L'],
        '6': ['M','N','O'],
        '7': ['P','Q','R','S'],
        '8': ['T','U','V'],
        '9': ['W','X','Y','Z']
    }
    ans =[""]
    def generate(pos, curAns):
        newAns = []
        for a in curAns:
            for k in map[phone_number[pos]]:
                newAns.append(a+k)
        return newAns
    for i in range(len(phone_number)):
       ans =  generate(i,ans)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
