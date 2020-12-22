from typing import List
import collections
import bisect
class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cube in cuboids:cube.sort()    
        _sort = sorted(cuboids)
        dp = [x[2] for x in _sort]
        for i in range(len(cuboids)):
            for j in range(i-1,-1,-1):
                if _sort[j][0]<=_sort[i][0] and _sort[j][1]<=_sort[i][1] and _sort[j][2]<=_sort[i][2]:
                    dp[i] = max(dp[i],dp[j]+_sort[i][2])
        return max(dp)


a = Solution()
in_para1 = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
in_para2 = "execution"
resu = a.maxHeight(in_para1)
print(resu)
