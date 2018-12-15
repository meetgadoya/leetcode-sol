def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    c = 0
    root = l3 = ListNode(0)

    while l1 or l2 or c:
        a = 0
        b = 0

        if l1:
            a = l1.val
            l1 = l1.next
        if l2:
            b = l2.val
            l2 = l2.next

        d = (a + b + c) % 10
        c = (a + b + c) / 10

        l3.next = ListNode(d)
        l3 = l3.next

    return root.next