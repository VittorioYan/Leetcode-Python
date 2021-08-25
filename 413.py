from typing import List
from collections import deque,defaultdict
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def f(x):
            return sum(range(x-1))
        n = len(nums)
        if n<3:
            return 0
        slice_length = []
        pos = 0
        diff = nums[1]-nums[0]
        for i in range(2,n):
            if nums[i]-nums[i-1]!=diff:
                if i-pos>=3:
                    slice_length.append(i-pos)
                pos = i-1
                diff = nums[i]-nums[i-1]
        if n-pos>=3:
            slice_length.append(n-pos)
        return sum([f(x) for x in slice_length])


a = Solution()
in_para1 =  [1,2,3,5,2,5,3,4,5,6,4,8,3,6,8,9,6,3]

in_para2 = [2,4]
resu = a.numberOfArithmeticSlices(in_para1)
print(resu)
