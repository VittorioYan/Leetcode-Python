from typing import List
import heapq


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        heapq._heapify_max(A)
        biggest, a, b = heapq._heappop_max(A), heapq._heappop_max(A), 0
        while A:
            b = heapq._heappop_max(A)
            if a+b<=biggest:
                biggest,a,b = a,b,0
            else:
                return a+b+biggest
        return 0


a = Solution()
in_para1 = [1,2,3]
in_para2 = 552
resu = a.largestPerimeter(in_para1)
print(resu)
