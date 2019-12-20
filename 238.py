from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums.copy()
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i] * nums[i - 1]
            res[n - i - 1] = res[n - i] * res[n - i - 1]
        for i in range(n):
            if i == 0:
                res[i] = res[i + 1]
                continue
            if i == n-1:
                res[i]=nums[i-1]
                break
            res[i] = res[i + 1] * nums[i - 1]
        return res


a = Solution()
in_para1 = [1, 2, 3, 4]
in_para2 = 9
resu = a.productExceptSelf(in_para1)
print(resu)
