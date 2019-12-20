from typing import List
import sys

class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        square_nums = []

        for i in range(1, n):
            cur = i ** 2
            if cur == n:
                return 1
            if cur > n:
                break
            square_nums.append(cur)
        dp = [n] * (n + 1)
        for square_num in square_nums:
            if square_num >= n:
                break
            dp[square_num] = 1
        for i in range(1, n + 1):
            if dp[i] == 1:
                continue
            mid = dp[i]
            for square_num in square_nums:
                if square_num > i:
                    break
                mid = min(mid, dp[i - square_num] + 1)
            dp[i] = mid

        return dp[-1]

a = Solution()
in_para1 = 8405
in_para2 = 9
resu = a.numSquares(in_para1)
print(resu)
