# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

####################################    PROGRAM: TO SORT A LINK LIST        ##################################################

######################################          TIME LIMIT EXCEEDED             ###########################################
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        mini = float("inf")
        h = head
        if (head == None):
            return None
        if (head.next == None):
            return head
        prev = None
        while (h != None):
            st = h
            # print()
            # print("h",h.val)
            mini_st = st.val
            mini = float("inf")

            #             find the minimum number
            while (st != None):
                mini = min(mini, st.val)
                st = st.next
            # print(mini)
            #           check whether is there any change
            if (mini == mini_st):
                prev = h
                h = h.next
                continue
            st = h
            while (st.next != None and st != None):
                if (st.next.val == mini):
                    ptr = st.next
                    st.next = ptr.next
                    ptr.next = h
                    if (h == head):
                        head = ptr
                        h = head
                    # h.next=ptr
                    else:
                        prev.next = ptr
                        h = ptr
                    continue
                else:
                    st = st.next
            prev = h
            h = h.next

        #             temp=head
        #             l=[]
        #             while(temp!=None):
        #                 l.append(temp.val)
        #                 temp=temp.next
        #             print("final result after iter",l)

        return head


###################################################################################################################
def sortList(self, head):
    if head is None or head.next is None:
        return head
    middle_node = self.find_middle_node(head)
    right_head = middle_node.next
    middle_node.next = None
    return self.merge(self.sortList(head), self.sortList(right_head))


def merge(head1, head2):
    dummy = ListNode(None)
    node = dummy
    while head1 and head2:
        if head1.val < head2.val:
            node.next = head1
            head1 = head1.next
        else:
            node.next = head2
            head2 = head2.next
        node = node.next

    node.next = head1 or head2
    return dummy.next


def find_middle_node(head):
    slow, fast = head, head
    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    return slow
