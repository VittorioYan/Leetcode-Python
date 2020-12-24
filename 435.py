from typing import List
import collections
import bisect

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        cur = intervals[0]
        ans = 0
        for i in range(1,len(intervals)):
            if intervals[i][0]==cur[0]:
                ans+=1
                continue
            if intervals[i][0]<cur[1]:
                ans+=1
                if cur[1]<intervals[i][1]:
                    continue
            cur = intervals[i]
        return ans


a = Solution()
in_para1 =[[1,2],[2,3]]
in_para2 = [2]
resu = a.eraseOverlapIntervals(in_para1)
print(resu)
