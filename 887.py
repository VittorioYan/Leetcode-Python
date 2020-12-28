from typing import List
import collections
import bisect
import math

# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         ans = 0
#         while K>1 and N>1:
#             N = int(N/2)
#             K-=1
#             ans+=1
#         ans += N
#         return ans 
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        memo = [[-1]*(N+1) for _ in range(K+1)]
        for i in range(N+1):
            memo[1][i] = i
            memo[0][i] = 0
        for i in range(K+1):
            memo[i][0] = 0

        for i in range(2,K+1):
            for j in range(1,N+1):
                li,hi = 1,j
                while li+1<hi:
                    mid = (hi+li)//2
                    if memo[i-1][mid-1]<memo[i][j-mid]:
                        li = mid
                    else:
                        hi = mid
                memo[i][j] = 1+min(memo[i-1][hi-1],memo[i][j-li])

                # for k in range(1,j+1):
                #     cur = min(cur,1+max(memo[i-1][k-1],memo[i][j-k]))
                # memo[i][j] = cur
        return memo[K][N]

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if K==1 or N==1:
            return N
        dp = [1]*(K+1)
        mid = dp.copy()
        j = 2
        while True:
            dp[1] = j
            for i in range(2,K+1):
                if i>j:
                    dp[i] = dp[i-1]
                    continue
                dp[i] = 1+mid[i-1]+mid[i]
                if dp[i] >= N:
                    return j
            mid = dp.copy()     
            j+=1
            

a = Solution()
in_para1 = 6
in_para2 = 6475
in_para1 = 2
in_para2 = 2
resu = a.superEggDrop(in_para1,in_para2)
print(resu)
