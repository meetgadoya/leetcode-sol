def findPeakElement(self, nums):
    temp = [float("-inf")] + nums + [float("-inf")]
    return self.search(temp, 1, len(nums) + 1)


def search(self, temp, i, j):
    mid = (i + j) // 2

    if (temp[mid] > temp[mid + 1] and temp[mid] > temp[mid - 1]):
        a = mid
        return mid - 1
    elif (temp[mid + 1] > temp[mid]):
        a = self.search(temp, mid + 1, j)
    else:
        a = self.search(temp, i, mid - 1)
    return a