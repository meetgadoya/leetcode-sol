
n = len(nums)
l = range(n + 1)

j = (list(set(l) - set(nums)))
return (j[0])
####################################    2nd method  ################################33

expected_sum = len(nums)*(len(nums)+1)//2
actual_sum = sum(nums)
return expected_sum - actual_sum