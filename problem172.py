class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeroCnt = 0
        while n > 0:
            n = n/5; zeroCnt += n
        
        return zeroCnt
