from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    a = b = c = 0
                    if i - 1 >= 0:
                        a = dp[i - 1][j]
                    if j - 1 >= 0:
                        b = dp[i][j - 1]
                    if i - 1 >= 0 and j - 1 >= 0:
                        c = dp[i - 1][j - 1]
                    dp[i][j] = min(a, b, c) + 1

        max_len = 0
        for i in range(m):
            max_len = max(max_len, max(dp[i]))
        return max_len * max_len


a = Solution()
in_para1 = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]

in_para2 = 2
resu = a.maximalSquare(in_para1)
print(resu)
