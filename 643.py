from typing import List
import bisect
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k>len(nums):
            return sum(nums)/k
        ans = sum(nums[:k])
        mid = ans
        for i in range(k,len(nums)):
            mid = mid+nums[i]-nums[i-k]
            ans = max(mid,ans)
        return ans/k

a = Solution()
in_para1 = [1,12,-5,-6,50,3]
in_para2 = 4
resu = a.findMaxAverage(in_para1,in_para2)
print(resu)
