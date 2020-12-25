from typing import List
import collections
import bisect

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-n+1]
        for i in range(n-2,-1,-1):
            cur = -(i+nums[i])
            pos = bisect.bisect_left(dp,cur)
            if len(dp)<=pos+1:
                dp.append(-i)
            else:
                dp = dp[:pos+1]+[-i]
        # print(dp)
        return len(dp)-1

        

a = Solution()
in_para1 = [2,3,1,0,4]
in_para2 = "execution"
resu = a.jump(in_para1)
print(resu)
