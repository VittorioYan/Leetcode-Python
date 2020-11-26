from typing import List
import sys
import functools


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(reverse=True, key=lambda x: x[1]-x[0])
        res = 0  # 以初始能量为0开始模拟
        val = 0  # 当前剩余能量
        for a, m in tasks:
            if m > val:  # 如果不能达到当前最低能量
                res += m - val
                val = m
            val -= a
        return res


a = Solution()
in_para1 = [[1, 1], [1, 3]]
in_para2 = 552
resu = a.minimumEffort(in_para1)
print(resu)
