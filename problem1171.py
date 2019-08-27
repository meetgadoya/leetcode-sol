'''
Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  You may return any such answer.



(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.

Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]

Example 3:
'''
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# logic: runtime=28 ms beats beats 89%
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr_sum = 0
        d = {}

        curr = head
        while curr:
            curr_sum += curr.val
            if curr_sum == 0:
                head = curr.next
            else:
                if curr_sum in d:
                    d[curr_sum].next = curr.next
                else:
                    d[curr_sum] = curr
            curr = curr.next
        return head