from typing import List
import collections
import bisect

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        cur_max,cur_min = nums[0],nums[0]
        pos_max,pos_min = 0,0
        l = r = 0
        ans = 1
        while r<len(nums):
            if nums[r]<=cur_min:
                pos_min = r
                cur_min = nums[r]
            if nums[r]>=cur_max:
                pos_max = r
                cur_max = nums[r]
            if cur_max-cur_min>limit:
                ans = max(ans,r-l)
                if cur_max==nums[r]:
                    l = r = pos_min+1
                    cur_max=cur_min = nums[r]
                elif cur_min==nums[r]:
                    l = r = pos_max+1
                    cur_max=cur_min = nums[r]
                continue
            r+=1
        ans = max(r-l,ans)
        return ans

            
a = Solution()
in_para1 = [8,2,4,7]
in_para2 = 4
resu = a.longestSubarray(in_para1,in_para2)
print(resu)
