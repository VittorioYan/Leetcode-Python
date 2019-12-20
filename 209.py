from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l = 0
        r = 1
        if not nums:
            return 0
        _sum = nums[0]
        lenn = len(nums)
        _min = lenn + 1
        while r <= lenn:
            if _sum >= s:
                _min = min(_min, r - l)
                _sum -= nums[l]
                l += 1
            else:
                if r >= lenn:
                    break
                _sum += nums[r]
                r += 1
        if _min == lenn + 1:
            return 0
        return _min


a = Solution()
in_para1 = 11
in_para2 = [1, 2, 3, 4, 5]
resu = a.minSubArrayLen(in_para1, in_para2)
print(resu)
