#############################################           JUMP GAME               ##################################################
#           USES RECURSION WITH DYNAMIC PROGRAMMING
#           TIME AND MEMORY LIMIT EXCEEDS
#           ONLY LAST CASE FAILS
import time
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    d = {}
    res = helper(nums, 0, 0, d)
    return res >= 1


def helper( nums, i, res, d):
    if nums[i] > len(nums) - i:
        return 1
    if i in d:
        return d[i]
    else:
        if (res >= 1):
            return 1
        if (i >= len(nums)):
            return 0
        if i == len(nums) - 1:
            return 1
        if nums[i] == 0:
            return 0
        for j in range(nums[i]):
            res = res + helper(nums, i + j + 1, res, d)
            if (res >= 1):
                return 1
        d[i] = res
        return res

#                   USING TWO FOR LOOPS
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 0 or len(nums) == 1:
        return True
    d = [0] * (len(nums))
    # if len(d)==0:
    #     return True
    d[-1] = 1
    # print(d)
    for i in range(len(nums) - 2, -1, -1):
        far_pt = min(nums[i] + i, len(nums) - 1)
        for j in range(i + 1, far_pt + 1, 1):
            if (d[j] == 1):
                d[i] = 1
                break

    return d[0] == 1

#           USING GREEDY SOLUTION IN O(N)
def canJump(nums):

    if (len(nums) < 2):
        return True
    last = len(nums) - 1

    for i in range(last - 1, -1, -1):
        if (i + nums[i] >= last):
            last = i

    return last == 0
