from typing import List
import collections
import bisect

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        len1,len2 = len(s1),len(s2)
        dp = [[0]*(len2+1) for _ in range(len1+1)]
        for i in range(1,len1+1):
            for j in range(1,len2+1):
                if s1[i-1]==s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+ord(s1[i-1])
                else:
                    dp[i][j] =max(dp[i][j-1],dp[i-1][j])
        
        return sum([ord(x) for x in s1+s2])-2*dp[len1][len2]

a = Solution()
in_para1 = "a"
in_para2 = "b"
resu = a.minimumDeleteSum(in_para1,in_para2)
print(resu)
