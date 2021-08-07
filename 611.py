from typing import DefaultDict, List
import collections
from collections import deque
import bisect
import heapq

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)
        while i<n and nums[i]==0:
            i+=1
        nums = nums[i:]
        n = len(nums)
        if n<3:
            return 0
        ans = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                min_3 = nums[i]+nums[j]
                pos = bisect.bisect_left(nums,min_3)
                ans+=pos-j-1
        return ans

a = Solution()
in_para1=  [2,2,3,4]
in_para2=[[0,2,2],[4,2,4],[2,13,1000000000]]
resu = a.triangleNumber(in_para1)

print(resu)
