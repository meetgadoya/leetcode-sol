import collections
import heapq
def topKFrequent(nums, k):

        count = collections.Counter(nums)
        print(count.get(k))
        return heapq.nlargest(k, count.keys(), key=count.get)

print(topKFrequent([3,2,2,1,1,1],2))