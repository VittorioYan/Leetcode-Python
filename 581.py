from typing import DefaultDict, List
import collections
from collections import deque
import bisect
import heapq
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l,r = -1,-1
        n = len(nums)
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                if l==-1:
                    l = i
                    r = i+1
                else:
                    r = i
        if l==-1:
            return 0
        mi,ma = min(nums[l:r+1]),max(nums[l:r+1])
        flag = True
        while flag:
            flag = False
            for i in range(l-1,-1,-1):
                if nums[i]>mi:
                    if nums[i]>ma:
                        ma = nums[i]
                        flag = True
                    l-=1
                else:
                    break

            for i in range(r+1,n):
                if nums[i]<ma:
                    if nums[i]<mi:
                        mi = nums[i]
                        flag = True
                    r+=1
                else:
                    break
        return r-l+1
            


a = Solution()
in_para1= [1,3,5,4,2]
in_para2=[[0,2,2],[4,2,4],[2,13,1000000000]]
resu = a.findUnsortedSubarray(in_para1)

print(resu)
