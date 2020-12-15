from typing import List

class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        def mid_handle(n:int):
            n_str = str(n)
            if n<10:
                return n
            flag = 0
            for i in range(1,len(n_str)):
                if n_str[i]<n_str[i-1]:
                    flag=i
                    break
            if flag:
                return int(str(mid_handle(int(n_str[:flag])-1))+'9'*(len(n_str)-flag))
            else:
                return n
        return mid_handle(N)



a = Solution()
in_para1 = 1234
in_para2 = 552
resu = a.monotoneIncreasingDigits(in_para1)
print(resu)
