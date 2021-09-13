from typing import List
import collections
import bisect
from functools import lru_cache
from collections import defaultdict
import math
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def dist(p1:List[int],p2:List[int]):
            return (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        length = defaultdict(dict)
        n = len(points)
        for i in range(1,n):
            for j in range(i):
                dis = dist(points[i],points[j])
                length[dis][i] = length[dis].get(i,0)+1
                length[dis][j] = length[dis].get(j,0)+1
        ans = 0
        for _,v in length.items():
            for _ ,item in v.items():
                ans += item*(item-1)
        return ans

a = Solution()
in_para1 =[[0,0],[1,0],[-1,0],[0,1],[0,-1]]
in_para2 = 1
resu = a.numberOfBoomerangs(in_para1)
print(resu)
