from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        count = len(primes)
        dp_num = [0] * count
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = min(primes[j] * dp[dp_num[j]] for j in range(count))
            for j in range(count):
                if dp[i] >= primes[j] * dp[dp_num[j]]:
                    dp_num[j] += 1
        print(dp)
        return dp[-1]


a = Solution()
in_para1 = [2, 7, 13, 19]
in_para2 = 12
resu = a.nthSuperUglyNumber(in_para2, in_para1)
print(resu)
