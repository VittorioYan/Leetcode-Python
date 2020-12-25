from typing import List
import collections
import bisect

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j,ans=len(g)-1,len(s)-1,0
        while i>=0 and j>=0:
            if s[j]>=g[i]:
                j-=1
                i-=1
                ans+=1
            else:
                i-=1
        return ans 
        

a = Solution()
in_para1 = [1]
in_para2 = [2]
resu = a.findContentChildren(in_para1,in_para2)
print(resu)
