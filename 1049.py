from typing import List, Sequence
import collections
import bisect
import heapq
from sortedcontainers import SortedList
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        S = sum(stones)
        target = S//2+1
        dp = [False]*target
        dp[0] = True
        for stone in stones:
            for i in range(target-1,stone-1,-1):
                if dp[i-stone]:
                    dp[i] = True
        for i in range(target-1,-1,-1):
            if dp[i]:
                return S-i*2

a = Solution()
in_para1 = [31,26,33,21,40]
in_para2 = 4
resu = a.lastStoneWeightII(in_para1)
print(resu)
