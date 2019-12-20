from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0]*len(nums)
        for i in range(len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        print(dp)
        mid = dp[-1]
        for i in range(len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        print(dp)
        return dp[-1] - mid


a = Solution()
in_para1 = [2,3,2]
in_para2 = 3
resu = a.rob(in_para1)
print(resu)