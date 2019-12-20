from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        使用Boyer-Moore 投票算法

        :param nums:
        """
        cal = 0
        now_maj = 0
        for num in nums:
            if cal == 0:
                now_maj = num
            if now_maj == num:
                cal += 1
            else:
                cal -= 1
        return now_maj

a = Solution()
in_para1 = [2,2,1,1,1,2,2]
in_para2 = -2147483648
resu = a.majorityElement(in_para1)
print(resu)