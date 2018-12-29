def lengthOfLIS(nums):
    Lis=[1]*len(nums)

    for  i in range(1,len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                Lis[i]=max(Lis[i],1+Lis[j])

    return(max(Lis))
print(lengthOfLIS([10,9,2,5,3,7,101,18]))