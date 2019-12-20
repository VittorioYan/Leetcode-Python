from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


a = Solution()
in_para1 = [1, 2, 3, 1]
in_para2 = 9
resu = a.containsDuplicate(in_para1)
print(resu)
