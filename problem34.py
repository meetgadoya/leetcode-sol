class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        st = 0
        end = len(nums) - 1

        # if(nums[0]==target and nums[-1]==target):
        #     return [0,len(nums)-1]

        if (target not in nums):
            return [-1, -1]
        if (nums[0] == target and nums[-1] == target):
            return [0, len(nums) - 1]

        while (st <= end):
            mid = (st + end) // 2
            if nums[mid] == target:
                i, j = mid, mid
                while (i >= st and nums[i] == target):
                    i = i - 1
                while (j <= end and nums[j] == target):
                    j = j + 1
                return [i + 1, j - 1]

            if target > nums[mid]:
                st = mid + 1
            else:
                end = mid - 1
        return [-1, -1]