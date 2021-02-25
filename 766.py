from typing import List, Sequence
import collections
import bisect
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m,n = len(matrix),len(matrix[0])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]!=matrix[i-1][j-1]:
                    return False
        return True
     

a = Solution()
in_para1 =[[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
in_para2 = "execution"
resu = a.isToeplitzMatrix(in_para1)
print(resu)
