from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        return nums.index(max(nums))


a = Solution()
in_para1 =[1,2,1,3,5,6,4]
resu = a.findPeakElement(in_para1)
print(resu)