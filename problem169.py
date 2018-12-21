def majorityElement(self, nums):

    nums.sort()
    return(nums[len(nums)//2])


######################################  2nd Method

import collections

def majorityElement(nums):
    counts = collections.Counter(nums)
    #print(counts)
    return max(counts.keys(), key=counts.get)

