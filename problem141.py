# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        if head.next == head:
            return True
        elif head.next == None:
            return False
        else:
            slow = head.next
            if (head.next.next != None):
                fast = head.next.next
            else:
                return False

        if (fast.next == slow):
            return True
        while (slow != fast):
            slow = slow.next
            if (fast == None or fast.next == None):
                return False
            fast = fast.next.next

        return True