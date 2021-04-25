from typing import List
class Solution:
    def clumsy(self, N: int) -> int:
        def assis(n:int):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 1
            if n==3:
                return 1
            if n==4:
                return -2
            return n-(n-1)*(n-2)//(n-3)+assis(n-4)

        if N<=2:
            return N
        if N==3:
            return 6
        if N==4:
            return 7
        return N*(N-1)//(N-2)+assis(N-3)


a = Solution()
in_para1 = 10
in_para2 = [1,0]
resu = a.clumsy(in_para1)
print(resu)
