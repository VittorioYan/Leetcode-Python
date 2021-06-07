from typing import DefaultDict, List
import collections
from collections import Counter
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)]
        for str in strs:
            cur_dic = Counter(str)
            num_0,num_1 = cur_dic['0'],cur_dic['1']
            for i in range(m,num_0-1,-1):
                for j in range(n,num_1-1,-1):
                    dp[i][j] = max(dp[i][j],dp[i-num_0][j-num_1]+1)

        return dp[-1][-1]
                

a = Solution()
in_para1 = "ababbc"
in_para2 = 2
resu = a.findMaxForm(in_para1)
print(resu)
