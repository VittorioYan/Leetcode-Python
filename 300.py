from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


a = Solution()
in_para1 = [1,3,6,7,9,4,10,5,6]
in_para2 = 9
resu = a.lengthOfLIS(in_para1)
print(resu)
