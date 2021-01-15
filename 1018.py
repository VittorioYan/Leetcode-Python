from typing import List
import heapq

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        cur = 0
        for a in A:
            cur = (cur*2+a)%5
            ans.append(cur==0)
        return ans


a = Solution()
in_para1 = [0,1,1,1,1,1]
in_para2 = 552
resu = a.prefixesDivBy5(in_para1)
print(resu)
