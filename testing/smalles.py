def smallest_nonconstructible_value(A: list[int]) -> int:
    def canMake(num,pos):
        if num == 0:
            return True
        elif num < 0 or pos >= len(A):
            return False
        return  canMake(num-A[pos],pos+1) or canMake(num, pos+1)
    # count = 1
    # while True:
    #     if not canMake(count,0):
    #         return count
    #     count += 1
print(smallest_nonconstructible_value([1, 2, 3, 4]))