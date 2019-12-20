from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        def deep_change(index):
            if index >= n or nums[index] == -1:
                return
            mid = nums[index]
            nums[index] = -1
            deep_change(mid)

        for i in range(n):
            if nums[i] != -1:
                deep_change(nums[i])
        for i in range(n):
            if nums[i] != -1:
                return i
        return n


a = Solution()
in_para1 = [0]
in_para2 = 9
resu = a.missingNumber(in_para1)
print(resu)
