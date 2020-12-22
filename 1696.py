from typing import List
import bisect

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        slen = len(nums)
        dp = [-10000]*slen
        dp[0] = nums[0]
        max_first = [nums[0]]
        for i in range(1,slen):
            dp[i] = max_first[-1]+nums[i]
            index = bisect.bisect_left(max_first,dp[i])
            max_first.insert(index,dp[i])
            if len(max_first)>k:
                index = bisect.bisect_left(max_first,dp[i-k])
                max_first.pop(index)
        return dp[-1]

a = Solution()
in_para1 = [1,-5,-20,4,-1,3,-6,-3]
in_para2 = 2
resu = a.maxResult(in_para1,in_para2)
print(resu)
