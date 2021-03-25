from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        a = a%1337
        cur = a**b[-1] %1337
        if len(b)==1:
            return cur
        return (cur*self.superPow(a,b[:-1])**10)%1337
        
        

a = Solution()
in_para1 = 2
in_para2 = [1,0]
resu = a.superPow(in_para1,in_para2)
print(resu)
