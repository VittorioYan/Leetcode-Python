from typing import List


class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ""
        if n < 26:
            return chr(n + 64)
        while n >= 26:
            n -= 1
            n, remainder = divmod(n, 26)
            res = chr(remainder + 65) + res
        if 0 < n < 26:
            res = chr(n + 64) + res
        return res


a = Solution()
in_para1 = 52
in_para2 = -2147483648
resu = a.convertToTitle(in_para1)
print(resu)