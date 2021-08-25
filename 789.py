from typing import List
import collections
import bisect
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        def length(start,end):
            return abs(start[0]-end[0]) + abs(start[1]-end[1])
        base = length(target,(0,0))
        for ghost in ghosts:
            if length(ghost,target)<=base:
                return False
        return True
        

a = Solution()
in_para1 =  [[1,0],[0,3]]
in_para2 = [0,1]
resu = a.escapeGhosts(in_para1,in_para2)
print(resu)
