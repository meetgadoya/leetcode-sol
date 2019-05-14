##########################              BRUTE FORCE O(N^2)      #############################################
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = len(nums) - 1

        while (i < j):
            a = i + 1
            while (a <= j and nums[i] <= nums[a]):
                a = a + 1
            if (a > j):
                i = i + 1
            else:
                break

        while (j > i):
            b = j - 1
            while (b >= i and nums[j] >= nums[b]):
                b = b - 1
            if (b < i):
                j = j - 1
            else:
                print(i, j)
                return j - i + 1
        return 0

########################################################################################################################
    public

    class Solution {
    public int findUnsortedSubarray(int[] nums) {
    int l = nums.length, r = 0;
    for (int i = 0; i < nums.length - 1; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[j] < nums[i]) {
                r = Math.max(r, j);
                l = Math.min(l, i);
            }
        }
    }

    return r - l < 0 ? 0: r - l + 1;
    }
    }


##########################                 USING SORTING           ############################################################
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums = sorted(nums)
        a = len(nums)
        b = 0

        for i in range(len(nums)):
            if (nums[i] != snums[i]):
                a = min(a, i)
                b = max(b, i)

        # print(a,b)
        if ((b - a) < 0):
            return 0
        return b - a + 1


##########################                 USING STACK           ############################################################
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)
        b = 0

        stack = []

        for i in range(len(nums)):
            while (len(stack) > 0 and nums[i] < nums[stack[-1]]):
                a = min(stack.pop(), a)
            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while (len(stack) > 0 and nums[i] > nums[stack[-1]]):
                b = max(stack.pop(), b)
            stack.append(i)

        if (a - b) > 0:
            return 0
        return b - a + 1


##########################                 USING CONSTANT SPACE O(N)           ############################################################
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a_num = float("inf")
        b_num = float("-inf")
        flag = False
        for i in range(1, len(nums)):
            if (nums[i] < nums[i - 1]):
                flag = True
            if (flag):
                a_num = min(nums[i], a_num)
        flag = False
        for i in range(len(nums) - 2, -1, -1):
            if (nums[i] > nums[i + 1]):
                flag = True
            if (flag):
                b_num = max(nums[i], b_num)

        for a in range(len(nums)):
            if (a_num < nums[a]):
                break
        for b in range(len(nums) - 1, -1, -1):
            if (b_num > nums[b]):
                break

        # print(a,b,a_num,b_num)
        if (a - b) >= 0:
            return 0
        return b - a + 1

