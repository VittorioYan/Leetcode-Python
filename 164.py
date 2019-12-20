from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        num_len = len(nums)
        if num_len < 2:
            return 0
        nums.sort()
        res = 0
        for i in range(1, num_len):
            res = max(res, nums[i] - nums[i-1])
        return res




a = Solution()
in_para1 =[3,6,9,1]
resu = a.maximumGap(in_para1)
print(resu)