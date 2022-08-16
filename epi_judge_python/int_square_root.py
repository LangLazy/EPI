from test_framework import generic_test

#Time O(logk)
def square_root(k: int) -> int:
    l,r = 0, k
    #r and onwards is too large
    #l and onwards is too small
    while l < r:
        mid = l + (r-l + 1)//2
        if mid**2 == k:
            return mid
        elif mid**2 > k:
            r = mid - 1
        else:
            l = mid ##If you do l + (r-l)//2 you will get stuck as it is left weighted so in a 2 elm
            #the mid elm will be the left one, so if you do l=mid you effectively have not shrunk anything
            #the soln is to right weight the mid calc
    return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
