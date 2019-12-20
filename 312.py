from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        def dfs(nums, i, j):
            if j <= i:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if j - i == 1:
                dp[i][j] = nums[i] * nums[i - 1] * nums[j]
                return dp[i][j]
            max_point = 0
            for k in range(i, j):
                cur_point = nums[k] * nums[i - 1] * nums[j]
                max_point = max(max_point, cur_point + dfs(nums, i, k) + dfs(nums, k + 1, j))
            dp[i][j] = max_point
            return dp[i][j]

        return dfs(nums, 1, n - 1)



a = Solution()
in_para1 = [3,1,5, 8]
in_para2 = 9
resu = a.maxCoins(in_para1)
print(resu)
