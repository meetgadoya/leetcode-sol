'''
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]


'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(set(nums2)) > len(set(nums1)):
            for a in set(nums1):
                if a in set(nums2):
                    res.append(a)
        else:
            for a in set(nums2):
                if a in set(nums1):
                    res.append(a)

        return res