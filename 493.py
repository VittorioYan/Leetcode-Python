from typing import List
import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sort_nums = []
        l = len(nums)
        ans = 0
        for i in range(l-1,-1,-1):
            pos = bisect.bisect_left(sort_nums, nums[i])
            ans+=pos
            bisect.insort_left(sort_nums,nums[i]*2)
        return ans


a = Solution()
in_para1 = [2, 4, 3, 5, 1]
in_para2 = 552
resu = a.reversePairs(in_para1)
print(resu)
