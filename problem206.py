def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    l = []
    if not head:
        return l
    r = head
    while (r != None):
        # print(r.val)
        l.append(r)
        r = r.next

    ##print (l)
    # l.pop()
    # print (l)
    h = l.pop()
    c = h
    while (len(l) > 0):
        b = l.pop()
        print(b.val)
        c.next = b
        c = b
        # print(len(l))
    # print(c.val)
    c.next = None
    return h