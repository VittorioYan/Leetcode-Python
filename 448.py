from typing import List
import collections
import bisect

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        def exchange(lis:list,a:int,b:int):
            mid = lis[a]
            lis[a] = lis[b]
            lis[b] = mid
        for i in range(n):
            while nums[i] != i+1:
                if nums[i]==nums[nums[i]-1]:
                    break
                exchange(nums,i,nums[i]-1)
        for i in range(n):
            if nums[i]!=i+1:
                ans.append(i+1)
        return ans
            
a = Solution()
in_para1 = [4,3,2,7,8,2,3,1]
in_para2 = [2]
resu = a.findDisappearedNumbers(in_para1)
print(resu)
