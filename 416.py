from typing import List
import collections
import bisect

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        aim = 0
        if _sum%2 ==1:
            return False
        else:
            aim = _sum//2
        dp = [False]*(aim+1)
        dp[0] = True
        for num in nums:
            for i in range(aim,num-1,-1):
                dp[i] = dp[i-num] or dp[i]
        return dp[aim]
        

a = Solution()
in_para1 =[2,2,1,8]
in_para2 = [2]
resu = a.canPartition(in_para1)
print(resu)
