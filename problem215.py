#print(nums)
l=heapq.nlargest(k,nums)
#for i in range(k-1):
    #heapq.largest(nums)
return l[-1]


#################################   2nd Method  ###############################3

nums.sort()
return nums[-k]