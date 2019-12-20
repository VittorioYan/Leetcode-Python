from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if not k or not nums:
            return
        k = k % n
        # nums = nums[:n-k]
        nums.extend(nums[:n-k])
        for i in range(n-k):
            nums.pop(0)
        # nums = nums[:n-k].append(nums[n-k+1:])



a = Solution()
in_para1 = [1,2,3,4,5,6,7]
in_para2 = 3
resu = a.rotate(in_para1, in_para2)
print(resu)