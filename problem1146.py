import copy


class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.nums = {}
        self.count = 0
        self.d = []

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.nums[index] = val

    def snap(self):
        """
        :rtype: int
        """

        self.d.append(self.nums.copy())
        return len(self.d) - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        if index in self.d[snap_id]:
            return self.d[snap_id][index]
        else:
            return 0

'''
Example 1:

Input: ["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5s
'''