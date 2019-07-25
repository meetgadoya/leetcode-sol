import time
# logic: trying my approach to take permutaion for every tens digit and finding mmaximum in it
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        d = {}
        ans = ""
        for i in nums:
            num = int(str(i)[0])
            if num not in d:
                d[num] = [str(i)]
            else:
                d[num].append(str(i))
        ad = sorted(d.items(), reverse=True)
        # print(d)

        for key, lis in ad:
            if key != 0:
                res = []
                self.combination(lis, "", res)
                ans = ans + str(max(res))
        if 0 in d:
            for item in d[0]:
                ans = ans + item

        return ans

    def combination(self, num_li, path, res):
        if not num_li:
            res.append(int(path))
        for i in range(len(num_li)):
            self.combination(num_li[:i] + num_li[i + 1:], path + num_li[i], res)
        # print(sorted(lis,reverse=True))

# logic 2 : more efficient approach
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        def func(x, y):
            if x + y < y + x: return 1
            if x + y > y + x: return -1
            return 0

        nums = sorted([str(x) for x in nums], key=cmp_to_key(func))
        return str(int(''.join(nums)))
obj = Solution()
st = time.time()
print(obj.largestNumber([41,23,87,55,50,53,18,9,39,63,35,33,54,25,26,49,74,61,32,81,97,99,38,96,22,95,35,57,80,80,16,22,17,13,89,11,75,98,57,81,69,8,10,85,13,49,66,94,80,25,13,85,55,12,87,50,28,96,80,43,10,24,88,52,16,92,61,28,26,78,28,28,16,1,56,31,47,85,27,30,85,2,30,51,84,50,3,14,97,9,91,90,63,90,92,89,76,76,67,55]))
end = time.time()
print(end-st)