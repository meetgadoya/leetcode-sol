'''
Example:

MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // returns 1
majorityChecker.query(0,3,3); // returns -1
majorityChecker.query(2,3,2); // returns 2

'''
# Bruteforce apporach
class MajorityChecker(object):

    def __init__(self, arr):
        """
        :type arr: List[int]
        """
        self.d = {}

        # self.li.append((0, arr[0]))
        # for i in range(1, len(arr)):
        #     if arr[i] == self.li[-1][1]:
        #         idx, num = self.li.pop()
        #         self.li.append((i, arr[i]))
        #     else:
        #         self.li.append((i, arr[i]))

        for i in range(len(arr)):
            self.d[i] = arr[i]
        # print(self.d)

    def query(self, left, right, threshold):
        """
        :type left: int
        :type right: int
        :type threshold: int
        :rtype: int
        """
        if left == right:
            return self.d[left]
        res = {}
        for i in range(left, right + 1):
            if self.d[i] in res:
                res[self.d[i]] += 1
                if res[self.d[i]] >= threshold:
                    # print(res)
                    return self.d[i]
            else:
                res[self.d[i]] = 1
        return -1


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
########################################################################################################################
# with the help of bisect function
########################################################################################################################

import collections
import bisect
import random
class MajorityChecker(object):

    def __init__(self, A):
        a2i = collections.defaultdict(list)
        for i, x in enumerate(A):
            a2i[x].append(i)
        self.A, self.a2i = A, a2i

        # print(self.A)
        # print(self.a2i)

    def query(self, left, right, threshold):
        for _ in range(10):
            a = self.A[random.randint(left, right)]
            l = bisect.bisect_left(self.a2i[a], left)
            r = bisect.bisect_right(self.a2i[a], right)
            print(left, right, a, self.a2i[a], l, r, threshold)
            if r - l >= threshold:
                print()
                return a
        return -1

# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)

########################################################################################################################
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.dp = collections.defaultdict(list)
        for i, v in enumerate(arr):
            self.dp[v].append(i)
        self.occur = sorted([(len(v), k) for k, v in self.dp.items()], reverse=True)
        # print(self.dp ,self.occur)

    def query(self, left: int, right: int, threshold: int) -> int:
        for o, v in self.occur:
            if o < threshold: break
            l = self.dp[v]
            low = bisect.bisect_left(l, left)
            high = bisect.bisect_right(l, right)
            if high - low >= threshold:
                return v
        return -1

    # Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)