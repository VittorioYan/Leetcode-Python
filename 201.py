from typing import List


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        bit_m = bin(m)[2:]
        bit_n = bin(n)[2:]
        index = 0
        if len(bit_m) == len(bit_n):
            while index < len(bit_m) and (bit_m[index] == bit_n[index]):
                index += 1
        else:
            return 0
        res = bit_m[:index] + "0" * (len(bit_m) - index)
        return int(res, 2)


a = Solution()
in_para1 = 10
in_para2 = 10
resu = a.rangeBitwiseAnd(in_para1, in_para2)
print(resu)
