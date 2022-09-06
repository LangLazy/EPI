from typing import List

from test_framework import generic_test

#Time O(len(words)*sum dicts) Space O(sum dicst)
def find_all_substrings(s: str, words: List[str]) -> List[int]:
    if not words:
        return []
    d = {}
    t = len(words) * len(words[0])
    ans = []
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    def attempt(pos):
        seen = {}
        done = 0
        while done < t:
            pot = s[pos:pos+len(words[0])]
            if pot in d and (pot not in seen or (pot in seen and seen[pot] < d[pot])):
                done += len(words[0])
                if pot in seen:
                    seen[pot] += 1
                else:
                    seen[pot] = 1
                pos += len(words[0])
            else:
                return False
        return True 
    for pos in range(0, len(s) - t+1):
        if attempt(pos):
            ans.append(pos)
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'string_decompositions_into_dictionary_words.py',
            'string_decompositions_into_dictionary_words.tsv',
            find_all_substrings))
