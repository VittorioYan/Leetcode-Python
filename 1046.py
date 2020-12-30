from typing import List
# import sys
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while len(stones)>1:
            a = heapq._heappop_max(stones)
            b = stones[0]
            if a==b:
                heapq._heappop_max(stones)
            else:
                heapq._heapreplace_max(stones,a-b)
        if len(stones)==0:
            return 0
        else:
            return stones[0]



a = Solution()
in_para1 = [2,7,4,1,8,1]
in_para2 = ["abcddefg"]
resu = a.lastStoneWeight(in_para1)
print(resu)
