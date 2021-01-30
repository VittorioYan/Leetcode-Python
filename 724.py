from typing import List, Sequence
import collections
import bisect

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all_num = sum(nums)
        cur = 0
        for index,num in enumerate(nums):
            if cur==all_num-num-cur:
                return index
            cur+=num
            if cur>all_num-num-cur:
                return -1
        return -1


a = Solution()
in_para1 = [1,2,3]
in_para2 = "execution"
resu = a.pivotIndex(in_para1)
print(resu)
