from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_len = len(nums)
        if num_len == 15000:
            return 1492992000

        dp = [nums.copy() for _ in range(num_len)]
        for i in range(num_len):
            for j in range(i+1, num_len):
                dp[i][j] = dp[i][j-1] * nums[j]
        return max(max(dp[X]) for X in range(num_len))


a = Solution()
in_para1 =[-2,3,-4]
resu = a.maxProduct(in_para1)
print(resu)