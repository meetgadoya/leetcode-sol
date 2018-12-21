import heapq


def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    l=[]
    for i in matrix:
        for j in i:
            l.append(j)
    print(l)
    l.sort()
    print(l)
    return l[k-1]
    #heapq.heapify(l)
    #print(list(l))

print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))
