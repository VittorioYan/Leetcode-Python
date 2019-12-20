from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        a = nums[:n // 2].copy()
        b = nums[n // 2:].copy()
        i = 0
        while a:
            nums[i] = a.pop()
            i += 1
            nums[i] = b.pop()
            i += 1
        if b:
            nums[i] = a[0]
        print(nums)


a = Solution()
in_para1 =[1, 5, 1, 1, 6, 4,3]
in_para2 = 9
a.wiggleSort(in_para1)
