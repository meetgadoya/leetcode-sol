#       NEXT PERMUTATAION

per_list = []
def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    org = nums
    nums=sorted(nums)
#     find the all possible permutation using permute
    per_func(nums,[])

    print(per_list)

    for i,per in enumerate(per_list):
        if per==org:
            loc=i

    if(loc==len(per_list)-1):
        return per_list[0]
    return per_list[loc+1]

def per_func(nums,tmp):
    if len(nums)==0:
        per_list.append(tmp)
        return
    for i in range(len(nums)):
        per_func(nums[:i]+nums[i+1:],tmp+[nums[i]])

##########################################      SOlN 2 IN SPACE     #######################################

i = len(nums) - 2
while (i >= 0 and nums[i] >= nums[i + 1]):
    i = i - 1

if (i >= 0):
    j = len(nums) - 1
    while (j >= i and nums[j] <= nums[i]):
        j = j - 1
    nums[i], nums[j] = nums[j], nums[i]
i = i + 1
j = len(nums) - 1

while (i < j):
    nums[i], nums[j] = nums[j], nums[i]
    i = i + 1
    j = j - 1
