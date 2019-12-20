from typing import List


class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        multi = 1
        for char in s[::-1]:
            res += (ord(char)-64) * multi
            multi *= 26
        return res

a = Solution()
in_para1 = "AAZ"
in_para2 = -2147483648
resu = a.titleToNumber(in_para1)
print(resu)