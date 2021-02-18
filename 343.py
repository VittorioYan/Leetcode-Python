from typing import List
# import sys

class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        if n==4:
            return 4
        if n==5:
            return 6
        if n==6:
            return 9
        return 3*self.integerBreak(n-3)



a = Solution()
in_para1 = 10
in_para2 = 9
resu = a.integerBreak(in_para1)
print(resu)
