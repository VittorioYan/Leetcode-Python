from typing import List
from sortedcontainers import SortedList

# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         pos = 1
#         queue = SortedList()
#         queue.add(1)
#         while pos<n:
#             now = queue[pos-1]
#             queue.add(now*2)
#             queue.add(now*3)
#             queue.add(now*5)
#             pos+=1
#         return queue[pos]

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        l_2 = 0
        l_3 = 0
        l_5 = 0
        for i in range(1, n):
            dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])
            if dp[i] >= 2 * dp[l_2]:
                l_2 += 1
            if dp[i] >= 3 * dp[l_3]:
                l_3 += 1
            if dp[i] >= 5 * dp[l_5]:
                l_5 += 1
        return dp[-1]


a = Solution()
in_para1 = 800
in_para2 = 9
resu = a.nthUglyNumber(in_para1)
print(resu)
