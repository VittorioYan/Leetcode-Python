from typing import List, Pattern
import collections
import bisect

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1)for _ in range(len(s)+1)]
        dp[0][0] = True
        j=1
        while j<len(p) and p[j]=='*':
            dp[0][j] = True
            dp[0][j+1] = True
            j+=2
        for j in range(1,len(p)+1):
            for i in range(1,len(s)+1):
                if p[j-1]=='*':
                    dp[i][j] = dp[i][j-1]
                    continue
                if j<len(p) and p[j]=='*':
                    if p[j-1]==s[i-1] or p[j-1]=='.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-1] or dp[i-1][j-1]
                    else:
                        dp[i][j] = dp[i][j-1]
                elif p[j-1]==s[i-1] or p[j-1]=='.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = False
        # print(dp)
        return dp[len(s)][len(p)]
        

a = Solution()
in_para1 = "ippi"
in_para2 = ".*p*p"
# in_para1 = "aab"
# in_para2 = "c*a*b"
resu = a.isMatch(in_para1,in_para2)
print(resu)
