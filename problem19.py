def removeNthFromEnd(self, head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    c = 0
    s = head
    while s != None:
        s = s.next
        c = c + 1
    if (c == 1):
        head = None
        return head

    i = c - n
    if (i == 0):
        head = head.next
        return head
    j = 0
    t = head
    s = head.next

    while (j < i - 1):
        t = t.next
        s = s.nexts
        j += 1

    t.next = s.next
    s.next = None

    return head