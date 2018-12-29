def rob(self, nums):
s = 0
i = 0
l = [-1] * len(nums)
a = self.hel(nums, i, l)
return a


def hel(self, nums, i, l):
    if (i < len(nums)):
        if (l[i] < 0):
            sa = max(nums[i] + self.hel(nums, i + 2, l), self.hel(nums, i + 1, l))
            l[i] = sa
        else:

            return l[i]
    else:
        return 0

    return sa