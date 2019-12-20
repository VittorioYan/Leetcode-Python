from typing import List
import sys


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        if not dungeon:
            return 1

        # m, n = len(dungeon), len(dungeon[0])
        # dungeon.append([0] * (n+1))
        # for i in range(m):
        #     dungeon[i].append(0)

        m, n = len(dungeon), len(dungeon[0])
        dp = [[0]*n for _ in range(m)]
        dp[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for i in range(m-2, -1, -1):
            dp[i][-1] = max(1, dp[i+1][-1] - dungeon[i][-1])
        for j in range(n-2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j+1] - dungeon[-1][j])
        for i in range(m-2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j])
        return dp[0][0]


        # for i in range(1, m):
        #     route[i][0] = route[i-1][0] + dungeon[i][0]
        #     dp[i][0] = min(dp[i-1][0], route[i][0])
        # for j in range(1, n):
        #     route[0][j] = route[0][j-1] + dungeon[0][j]
        #     dp[0][j] = min(dp[0][j-1], route[0][j])
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = min(dp[i][j-1], dp[i][j-1], route[i-1][j]+dungeon[i][j], route[i][j-1]+dungeon[i][j])
        #         route[i][j] = max(dp[i][j - 1], dp[i][j - 1], route[i - 1][j] + dungeon[i][j], route[i][j - 1] + dungeon[i][j])
        #         dp_left = min(dp[i][j-1], route[i][j-1] + dungeon[i][j])
        #         dp_up = min(dp[i-1][j], route[i-1][j] + dungeon[i][j])
        #         if dp_left < dp_up:
        #             route[i][j] = route[i-1][j] + dungeon[i][j]
        #             dp[i][j] = dp_up
        #         else:
        #             route[i][j] = route[i][j-1] + dungeon[i][j]
        #             dp[i][j] = dp_left

        if dp[-1][-1] >= 0:
            return 1
        else:
            return 1-dp[-1][-1]




a = Solution()
in_para1 = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
in_para2 = 452137076
resu = a.calculateMinimumHP(in_para1)
print(resu)