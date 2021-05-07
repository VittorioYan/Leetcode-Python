from typing import DefaultDict, List
import collections
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans^=start+2*i
        return ans



a = Solution()
in_para1 =  [11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]
in_para2 = 2
resu = a.xorOperation(5,0)
print(resu)
