from typing import List
import collections
import bisect
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            #print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [int(x) for x in matrix[0]]
        ans = self.largestRectangleArea(dp)
        for i in range(1,len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]=='0':
                    dp[j] = 0
                else:
                    dp[j]+=1
            ans = max(ans,self.largestRectangleArea(dp))
        return ans
                  

a = Solution()
in_para1 = [["0","0"]]
in_para2 = "execution"
resu = a.maximalRectangle(in_para1)
print(resu)
