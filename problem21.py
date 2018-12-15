def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    p = l1
    q = l2
    if (p == None):
        return q
    if (q == None):
        return p
    if (p.val < q.val):
        head = r = ListNode(p.val)
        p = p.next
    else:
        head = r = ListNode(q.val)
        q = q.next
    while p != None and q != None:
        if (p.val < q.val):
            s = ListNode(p.val)
            r.next = s
            p = p.next
        else:
            s = ListNode(q.val)
            r.next = s
            q = q.next
        r = s
    while p != None:
        s = ListNode(p.val)
        r.next = s
        p = p.next
        r = s
    while q != None:
        s = ListNode(q.val)
        r.next = s
        q = q.next
        r = s
    return head