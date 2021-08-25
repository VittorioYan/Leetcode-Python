from typing import Counter, List
from collections import deque,defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n<3:
            return 0
        dp = []
        ans = 0
        for i in range(n):
            dp.append(defaultdict(int))
            for j in range(i):
                cur = nums[i]-nums[j]
                dp[i][cur] += dp[j][cur]+1
                ans += dp[j][cur]
        return ans

a = Solution()
in_para1 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
in_para2 = [2,4]
resu = a.numberOfArithmeticSlices(in_para1)
print(resu)
