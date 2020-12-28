from typing import List
import collections
import bisect
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        size = len(piles)
        s = [0]*(size+1)
        dp = {}
        for i in range(size-1,-1,-1):
            s[i] = s[i+1]+piles[i]
        def dfs(i,M):
            if (i,M) in dp:
                return dp[(i,M)]
            if i>=size:
                return 0
            if i+M*2>=size:
                return s[i]
            best = 0
            for x in range(1,M*2+1):
                best = max(best,s[i]-dfs(i+x,max(x,M)))
            dp[(i,M)] = best
            return best
        return dfs(0,1)
        print(dp)
               

a = Solution()
in_para1 = [2,7,9,4,4]
in_para2 = "execution"
resu = a.stoneGameII(in_para1)
print(resu)
