from typing import List

class Solution:
    def fib(self, n: int) -> int:
        if n<1:
            return 0
        cur=a = 0
        b = 1
        for _ in range(n):
            cur = a+b
            a,b = cur,a
        return cur

a = Solution()
in_para1 = 30
in_para2 = 2
resu = a.fib(in_para1)
print(resu)
