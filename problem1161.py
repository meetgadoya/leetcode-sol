'''
Example 1:

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []
        floor = [root]

        # finding the level order traversal
        while floor:
            ans.append([node.val for node in floor])
            temp = []
            for node in floor:
                temp.extend([node.left, node.right])

            floor = [node for node in temp if node]

        # print(ans) [[1], [7, 0], [7, -8]]
        # now finding each level sum
        max_sum = -float('inf')
        max_idx = -float('inf')
        for i, li in enumerate(ans):
            if sum(li) > max_sum:
                max_sum = sum(li)
                max_idx = i
        return max_idx + 1