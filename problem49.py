import collections
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    #print(ans.values())
    for s in strs:
        print(tuple(sorted(s)))
        ans[tuple(sorted(s))].append(s)

    return ans.values()

###################################     2nd Method  ###################################


def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        ans[tuple(count)].append(s)
    return ans.values()


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))