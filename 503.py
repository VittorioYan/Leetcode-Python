from typing import DefaultDict, List
import collections

import heapq
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        small_first = [(nums[0],0)]
        ans = [-1]*len(nums)
        for index,num in enumerate(nums[1:]):
            cur = small_first[0]
            while cur[0]<num:
                ans[cur[1]] = num
                heapq.heappop(small_first)
                if small_first:
                    cur = small_first[0]
                else:
                    break
            heapq.heappush(small_first,(num,index+1))
        
        for index,num in enumerate(nums):
            cur = small_first[0]
            while cur[0]<num:
                ans[cur[1]] = num
                heapq.heappop(small_first)
                if len(small_first)>1:
                    cur = small_first[0]
                else:
                    break
            if len(small_first)<=1:
                break
        return ans


a = Solution()
in_para1 =  [1]
in_para2 = 2
resu = a.nextGreaterElements(in_para1)
print(resu)
