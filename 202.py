from typing import List


class Solution:
    def isHappy(self, n: int) -> bool:
        is_meet = set()

        def meeting(num):
            if num in is_meet:
                return False
            if num == 1:
                return True
            is_meet.add(num)
            new_num = 0
            while num > 0:
                new_num += (num % 10) ** 2
                num //= 10
            return meeting(new_num)
        return meeting(n)

a = Solution()
in_para1 = 19
in_para2 = 10
resu = a.isHappy(in_para1)
print(resu)
