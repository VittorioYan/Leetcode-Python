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
        

a = Solution()
in_para1 = [2,1,5,6,2,3]
in_para2 = "execution"
resu = a.maxEnvelopes(in_para1)
print(resu)
