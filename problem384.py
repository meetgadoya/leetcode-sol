class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        self.n = nums

        self.d = nums
        self.temp = []

        # print(d)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        # global nums
        self.arr = self.n
        return (self.arr)

    def shuffle(self):
        aux = list(self.n)
        self.temp = []

        while len(aux) > 0:
            a = random.choice(aux)
            aux.remove(a)
            self.temp.append(a)

        return self.temp

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()