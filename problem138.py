#https://www.youtube.com/watch?v=EHpS2TBfWQg
#https://www.youtube.com/watch?v=OvpKeraoxW0
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

#logic: runtime = 376ms beats 98%
def copyRandomList(self, head):
    """
    :type head: Node
    :rtype: Node
    """
    if not head:
        return head
    h = head
    # creating a duplicate link list
    while h != None:
        new_node = Node(h.val, None, None)
        new_node.next = h.next
        h.next = new_node
        h = h.next.next

    # assigning random pointer
    h = head
    while h != None:
        if h.random != None:
            h.next.random = h.random.next
        h = h.next.next

    old_head = head
    new_head = head.next
    return_head = new_head

    while new_head.next != None:
        old_head.next = new_head.next
        old_head = old_head.next
        new_head.next = old_head.next
        new_head = new_head.next

    new_head.next = None
    old_head.next = None
    return return_head
