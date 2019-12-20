from typing import List
import sys


class Solution:
    def countDigitOne(self, n: int) -> int:
        dig_num = [0, 1]
        multi = 1
        if n < 0:
            return 0
        for i in range(50):
            multi *= 10
            if multi > sys.maxsize:
                break
            dig_num.append(multi + dig_num[-1] * 10)
        n_str = str(n)

        def assist(sn: str):
            nonlocal dig_num
            if len(sn) == 1:
                if sn[0] == '0':
                    return 0
                else:
                    return 1
            cur_dig = int(sn[0])
            if cur_dig == 0:
                return assist(sn[1:])
            if cur_dig == 1:
                return dig_num[len(sn) - 1] + int(sn[1:]) + 1 + assist(sn[1:])
            return (cur_dig*dig_num[len(sn) - 1])+int('1'+'0'*(len(sn)-1)) + assist(sn[1:])

        return assist(n_str)


a = Solution()
in_para1 = -1
in_para2 = 9
resu = a.countDigitOne(in_para1)
print(resu)
