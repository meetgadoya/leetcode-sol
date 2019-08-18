class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # either make all odd places smaller or all even  places smaller
        res = [0,0]
        A = [float('inf')] + nums + [float('inf')]
        for i in range(1, len(A)-1):
            diff = max(0, A[i] - min(A[i+1], A[i-1]) + 1)
            res[i%2] += diff
        return min(res)
            
        
