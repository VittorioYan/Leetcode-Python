from typing import List
import sys

class Solution:
    def minCut(self, s: str) -> int:
        min_s = list(range(len(s)))
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
                    # 说明不用分割
                    if j == 0:
                        min_s[i] = 0
                    else:
                        min_s[i] = min(min_s[i], min_s[j - 1] + 1)
        return min_s[-1]


        # min_step = len(s) + 1
        # s_len = len(s)
        # dp = [[False]*s_len for _ in range(s_len)]
        # min_step_mat = [[min_step]*s_len for _ in range(s_len)]
        # for i in range(s_len):
        #     dp[i][i] = True
        #
        # for i in range(s_len-1, -1, -1):
        #     for j in range(s_len-1, -1, -1):
        #         if dp[i][j]:
        #             min_step_mat[j][i] = 1
        #         else:
        #             for k in range(j, i):
        #                 min_step_mat[j][i] = min(min_step_mat[j][i],
        #                                          min_step_mat[j][k]+min_step_mat[k+1][i])
        #


        # for i in range(1, s_len):
        #     for j in range(i):
        #         if s[i] == s[j] and (i-j < 2 or dp[j+1][i-1]):
        #             dp[j][i] = True
        #
        # for i in range(s_len):
        #     for j in range(i+1):
        #         if dp[j][i]:
        #             min_step_mat[j][i] = 1
        #         else:
        #             for k in range(j, i):
        #                 min_step_mat[j][i] = min(min_step_mat[j][i],
        #                                          min_step_mat[j][k]+min_step_mat[k+1][i])

        # def helper(cur_index, cur_step):
        #     nonlocal min_step
        #     if min_step_mat[cur_index] != s_len+1:
        #         helper(s_len + 1, cur_step + min_step_mat[cur_index])
        #
        #     print(cur_index, cur_step)
        #     if cur_index >= s_len:
        #         if cur_step < min_step:
        #             min_step = cur_step
        #         return
        #     if cur_step >= min_step:
        #         return
        #     for i in range(s_len-1, cur_index-1, -1):
        #         if dp[cur_index][i]:
        #             helper(i+1, cur_step+1)
        #     if min_step_mat[cur_index] > cur_step:
        #         min_step_mat[cur_index] = cur_step
        #
        # helper(0,  0)
        # return min_step_mat[0][s_len-1]


a = Solution()
graph = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"

print(a.minCut(graph))
