from typing import List
import collections
import bisect
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1,len(dp)):
            dp[i] = max(dp[i-1]+nums[i],dp[i])
        return (max(dp))
        

a = Solution()
in_para1 = [-2,1,-3,4,-1,2,1,-5,4]
in_para2 = "execution"
resu = a.maxSubArray(in_para1)
print(resu)
