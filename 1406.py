from typing import List
import collections
import bisect
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        size = len(stoneValue)
        s = [0]*(size+1)
        dp = [float('-inf')]*size
        aim = sum(stoneValue)/2
        for i in range(size-1,-1,-1):
            s[i] = s[i+1]+stoneValue[i]
        def dfs(i):
            if i>=size:
                return 0
            if dp[i]!=float('-inf'):
                return dp[i]
            best = float('-inf')
            for x in range(1,4):
                best = max(best,s[i]-dfs(i+x))
            dp[i] = best
            return best
        ans = dfs(0)

        if ans>aim:
            return 'Alice'
        elif ans == aim:
            return 'Tie'
        else:
            return 'Bob'


a = Solution()
in_para1 =[1,2,3,7]
in_para2 = "execution"
resu = a.stoneGameIII(in_para1)
print(resu)
