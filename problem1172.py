'''
You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

    DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
    void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.
    int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all stacks are empty.
    int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack, and returns -1 if the stack with that given index is empty.

Example:

Input:
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
Output:
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

Explanation:
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3
                                                        ﹈ ﹈
D.pop()            // Returns 4.  The stacks are now:   1  3
                                                        ﹈ ﹈
D.pop()            // Returns 3.  The stacks are now:   1
                                                        ﹈
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.

'''

# logic: runtime 856 ms beats 96%
import heapq
class DinnerPlates(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.stack = []
        self.lookup_push = []  # heap

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.lookup_push:
            idx = heapq.heappop(self.lookup_push)
            self.stack[idx].append(val)
            return
        elif len(self.stack) > 0:
            if len(self.stack[-1]) < self.capacity:
                self.stack[-1].append(val)
                return
        self.stack.append([val])

    def pop(self):
        """
        :rtype: int
        """
        while len(self.stack) > 0 and len(self.stack[-1]) == 0:
            self.stack.pop()

        if self.stack:
            res = self.stack[-1].pop()
            return res
        return -1

    def popAtStack(self, index):
        """
        :type index: int
        :rtype: int
        """
        ans = -1
        if index < len(self.stack) and len(self.stack[index]) > 0:
            ans = self.stack[index].pop(-1)
            heapq.heappush(self.lookup_push, index)
        return ans

# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)