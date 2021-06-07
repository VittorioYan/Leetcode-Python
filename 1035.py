from typing import List
import collections
import bisect
import heapq

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*(len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(1,len(nums1)+1):
            for j in range(1,len(nums2)+1):
                cur = -1
                if nums1[i-1]==nums2[j-1]:
                    cur = dp[i-1][j-1]+1
                dp[i][j] = max(cur,dp[i-1][j],dp[i][j-1])
                
        return dp[-1][-1]


a = Solution()
in_para1 = [1,4,2]
in_para2 = [1,2,4]
resu = a.maxUncrossedLines(in_para1,in_para2)
print(resu)
