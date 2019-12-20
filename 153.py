from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)


a = Solution()
in_para1 =[-2,3,-4]
resu = a.maxProduct(in_para1)
print(resu)