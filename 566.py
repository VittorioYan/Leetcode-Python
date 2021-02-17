from typing import List
import collections
import bisect

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m,n = len(nums),len(nums[0])
        if m*n!=r*c:
            return nums
        ans = []
        cur = []
        for i in range(m):
            for j in range(n):
                cur.append(nums[i][j])
                if len(cur)==c:
                    ans.append(cur)
                    cur=[]
        return ans
            
a = Solution()
in_para1 = [[1,2],[3,4]]
in_para2 = [2]
resu = a.matrixReshape(in_para1,1,4)
print(resu)
