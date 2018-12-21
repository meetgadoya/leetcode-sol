def oddEvenList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if (not head):
        return []
    oh = head
    evenh = head.next
    e = evenh
    o = head

    while (e != None and e.next != None):
        o.next = e.next
        o = e.next
        e.next = o.next
        e = o.next

    o.next = evenh
    return head

