from typing import List
import collections
import bisect

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size<2:
            return size
        dp = [1]*size
        for i in range(1,size):
            if nums[i]>nums[i-1]:
                dp[i] = dp[i-1]+1
        return max(dp)

        
a = Solution()
in_para1 =   [2,2,2,2]
in_para2 = [[0,1,2],[0,2,5]]
resu = a.findLengthOfLCIS(in_para1)
print(resu)
