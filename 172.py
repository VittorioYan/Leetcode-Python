from typing import List
import sys

class Solution:
    def trailingZeroes(self, n: int) -> int:
        cur_num = 5
        five_list = []

        while cur_num < sys.maxsize:
            five_list.append(cur_num)
            cur_num *= 5
        five_num = [1]
        for i in range(1, len(five_list)):
            five_num.append(five_num[-1] * 5 + 1)
        num_5 = 0
        continue_flag = True
        while continue_flag:
            continue_flag = False
            for i in range(len(five_list)-1, -1, -1):
                if five_list[i] <= n:
                    n -= five_list[i]
                    num_5 += five_num[i]
                    continue_flag = True
                    break
        return num_5


a = Solution()
in_para1 = 1808548329
in_para2 = 452137076
resu = a.trailingZeroes(in_para1)
print(resu)