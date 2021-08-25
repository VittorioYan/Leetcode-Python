from typing import List
import collections
import bisect
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        realation = [[-1]*n for _ in range(n)]
        for i in range(n):
            for j in range(n-1):
                realation[i][preferences[i][j]] = j
        pp = {}
        for a,b in pairs:
            pp[a] = b
            pp[b] = a

        def get_value(k,v):
            return realation[k][v]
        ans = 0
        for a,b in pp.items():
            pos_b = realation[a][b]
            for i in range(pos_b):
                cur = preferences[a][i]
                if get_value(cur,pp[cur])>get_value(cur,a):
                    ans+=1
                    break
        return ans 


a = Solution()
in_para1 = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
in_para2 = [[0, 1], [2, 3]]
resu = a.unhappyFriends(4,in_para1,in_para2)
print(resu)
