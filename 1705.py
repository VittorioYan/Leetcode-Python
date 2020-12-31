from typing import List
# import sys
import heapq
import collections
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        rot = []
        ans = 0
        i=0
        while rot or i<n:
            if i<n and apples[i]!=0:
                heapq.heappush(rot,(i+days[i],apples[i]))
            if not rot:
                i+=1
                continue
            cur = heapq.heappop(rot)
            while cur[0]<=i and rot:
                cur = heapq.heappop(rot)
            if cur[0]>i:
                ans+=1
                if cur[1]>1:
                    heapq.heappush(rot,(cur[0],cur[1]-1))
            i+=1
        return ans 

a = Solution()
in_para1 = [3,0,0,0,0,2]
in_para2 = [3,0,0,0,0,2]
resu = a.eatenApples(in_para1,in_para2)
print(resu)
