from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        num_zeros = 0
        for i in range(n):
            if nums[i] == 0:
                num_zeros+=1
                continue
            nums[i-num_zeros] = nums[i]
        for i in range(num_zeros):
            nums[-i-1] = 0
        print(nums)



a = Solution()
in_para1 = [0,1,0,3,12]
in_para2 = 9
resu = a.moveZeroes(in_para1)
print(resu)
