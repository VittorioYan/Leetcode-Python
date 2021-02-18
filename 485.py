from typing import List
import collections
import bisect

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = cur = 0
        for num in nums:
            if num==1:
                cur+=1
            else:
                ans = max(ans,cur)
                cur = 0
        ans = max(ans,cur)
        return ans
            
a = Solution()
in_para1 = [1,1,0,1,1,1]
in_para2 = [2]
resu = a.findMaxConsecutiveOnes(in_para1)
print(resu)
