def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    st = []
    end = []
    for l in sorted(intervals):
        st.append(l[0])
        end.append(l[1])

    ans = []
    # print(st)
    # print(end)
    while len(st) > 0:
        temp = []
        # print(ans)
        st_int = st.pop(0)
        temp.append(st_int)

        if (len(st) == 0):
            temp.append(end[-1])
            ans.append(temp)
            return ans

        while st[0] < end[0]:
            # print(st[0], end[0])
            st_int = st.pop(0)
            if (len(st) == 0):
                temp.append(end[-1])
                ans.append(temp)
                return ans

        while len(end) > len(st):
            end_int = end.pop(0)
        temp.append(end_int)
        print(temp)
        ans.append(temp)

    return ans


print(merge([[1,3],[8,10],[15,18],[2,6]]))