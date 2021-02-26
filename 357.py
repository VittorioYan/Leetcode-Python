from typing import Counter, List
import collections
import bisect
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        res = 10
        k = 9
        temp = 9
        for _ in range(2, min(n + 1, 11)):
            temp *= k
            k -= 1
            res += temp
        return res

        
a = Solution()
in_para1 =2
in_para2 =[2,2]
resu = a.countNumbersWithUniqueDigits(in_para1)
print(resu)
