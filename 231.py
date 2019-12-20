from typing import List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        if n == 1:
            return True
        if n % 2 == 0:
            return self.isPowerOfTwo(n // 2)
        return False


a = Solution()
in_para1 = 16
in_para2 = 9
resu = a.isPowerOfTwo(in_para1)
print(resu)
