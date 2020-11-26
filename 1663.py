from typing import List
# import sys


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        z_num = int((k-n)/25)
        if z_num==n:
            return 'z'*n
        a_num = int(n-z_num-1)
        which_char = chr(ord('a')-1+k-26*z_num-a_num)
        return 'a'*a_num+which_char+'z'*z_num



a = Solution()
in_para1 = 24
in_para2 = 552
resu = a.getSmallestString(in_para1, in_para2)
print(resu)
