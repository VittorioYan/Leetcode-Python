from typing import List
import collections
import bisect

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cur = nums[0]
        i=1
        while cur<len(nums)-1:
            if i>cur:
                return False
            cur = max(cur,i+nums[i])
            i+=1
        if cur>=len(nums)-1:
            return True
        return False

        

a = Solution()
in_para1 = [2,1,1,0,10]
in_para2 = "execution"
resu = a.canJump(in_para1)
print(resu)
