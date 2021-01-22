from typing import List
import collections
import bisect
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        def multiple(n:list):
            res = 1
            for item in n:
                res*=item
            return res
        if len(nums)<=3:
            return multiple(nums)
        nums.sort()
        # size = len(nums)
        # pos0 = bisect.bisect_left(nums,0)
        return max(multiple(nums[-3:]),nums[0]*nums[1]*nums[-1],nums[-1]*nums[-2]*nums[0])

        

a = Solution()
in_para1 = [-1,2,4]
in_para2 = 5
resu = a.maximumProduct(in_para1)
print(resu)
