from typing import List
import bisect
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                count+=1
                if i==1 or nums[i]>=nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return count<=1

a = Solution()
in_para1 = [1,2,-1,0]
in_para2 = "acde"
resu = a.checkPossibility(in_para1)
print(resu)
