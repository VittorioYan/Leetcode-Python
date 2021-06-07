from typing import List
import collections
import bisect
import heapq

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        maxnum = -1
        n = len(nums)
        ans = 0
        while maxnum!=0:
            maxnum = -1
            cur_1 = 0
            for index,num in enumerate(nums):
                cur_1 += num%2
                nums[index] = num>>1
                maxnum = max(maxnum,nums[index])
            ans += cur_1*(n-cur_1)
        return ans



a = Solution()
in_para1 = [4, 14, 2]
in_para2 = [1,2,4]
resu = a.totalHammingDistance(in_para1)
print(resu)
