from typing import List
import bisect


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # if not nums:
        #     return [-1,-1]
        left = bisect.bisect_left(nums,target)
        if left==len(nums) or nums[left]!=target:
            return [-1,-1]
        right = bisect.bisect_right(nums, target)-1
        return [left,right]


a = Solution()
in_para1 = []
in_para2 = 5
resu = a.searchRange(in_para1,in_para2)
print(resu)
