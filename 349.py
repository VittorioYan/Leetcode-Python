from typing import Counter, List
import collections
import bisect
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1,s2 = set(nums1),set(nums2)
        ans = []
        if len(s1)<len(s2):
            aim = s2
            iters = s1
        else:
            aim = s1
            iters = s2
        for i in list(iters):
            if i in aim:
                ans.append(i)
        return ans
        
a = Solution()
in_para1 =[1,1,1,2,2,3]
in_para2 =[2,2]
resu = a.intersection(in_para1,in_para2)
print(resu)
