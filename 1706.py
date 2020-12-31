from typing import List
# import sys
import heapq
import collections
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m,n  = len(grid),len(grid[0])
        def find_next(i,j,from_dest):
            # from_dest:0:up,1:right,2:down,3:left
            if  grid[i][j]==1:
                if from_dest==0:return 1
                if from_dest==1:return -1
                if from_dest==2:return -1
                if from_dest==3:return 2
            else:
                if from_dest==0:return 3
                if from_dest==1:return 2
                if from_dest==2:return -1
                if from_dest==3:return -1
        def handle(pos):
            i = 0
            j = pos
            from_dest = 0
            while 0<=j<n and 0<=i<m:
                ans = find_next(i,j,from_dest)
                if ans ==-1:
                    return -1
                if ans == 1:
                    j+=1
                    from_dest = 3
                if ans ==2:
                    i+=1
                    from_dest = 0
                if ans ==3:
                    j-=1
                    from_dest = 1
            if j>=n or j<0:
                return -1
            else:
                return j
        return [handle(x) for x in range(n)]
                

a = Solution()
in_para1 = [[-1]]
in_para2 = [3,0,0,0,0,2]
resu = a.findBall(in_para1)
print(resu)
