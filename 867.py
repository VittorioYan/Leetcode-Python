from typing import Counter, List
import collections
import bisect
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix),len(matrix[0])
        ans = []
        for i in range(n):
            cur = []
            for j in range(m):
                cur.append(matrix[j][i])
            ans.append(cur)
        return ans
        
a = Solution()
in_para1 =[[1]]
in_para2 = [0]
resu = a.transpose(in_para1)
print(resu)
