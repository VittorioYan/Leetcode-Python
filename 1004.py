from typing import List
# import sys
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        size = len(A)
        l = r = 0
        cur = 0
        ans = 0
        while r<size:
            if A[r]==0:
                cur+=1
            while cur>K:
                if A[l]==0:
                    cur-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans

a = Solution()
in_para1 =[1,1,1,0,0,0,1,1,1,1,0]
in_para2 = 2
resu = a.longestOnes(in_para1,in_para2)
print(resu)
