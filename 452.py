from typing import List
import collections
import bisect

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort()
        cur = points[0]
        ans = 1
        for i in range(1,len(points)):
            if points[i][0]<=cur[1]:
                cur = [max(cur[0],points[i][0]),min(cur[1],points[i][1])]
            else:
                ans+=1
                cur = points[i]
        return ans
            


a = Solution()
in_para1 =[[10,16],[2,8],[1,6],[7,12]]
in_para2 = [2]
resu = a.findMinArrowShots(in_para1)
print(resu)
