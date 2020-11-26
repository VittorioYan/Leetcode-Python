from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        output = 0
        i = 0
        while miss < n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                output += 1
                miss += miss
        return output


a = Solution()
in_para1 = [1, 2, 3, 8]
in_para2 = 80
resu = a.minPatches(in_para1, in_para2)
print(resu)
