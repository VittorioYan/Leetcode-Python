from typing import List


# class Solution:
#     def minPatches(self, nums: List[int], n: int) -> int:
#         miss = 1
#         output = 0
#         i = 0
#         while miss < n:
#             if i < len(nums) and nums[i] <= miss:
#                 miss += nums[i]
#                 i += 1
#             else:
#                 output += 1
#                 miss += miss
#         return output
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        cur,pos = 0,0
        while cur <n:
            if pos<len(nums) and nums[pos]<= cur+1:
                cur +=nums[pos]
                pos+=1
            else:
                print(cur+1)
                ans+=1
                cur = cur+1+cur
        return ans


a = Solution()
in_para1 = []
in_para2 = 8
resu = a.minPatches(in_para1, in_para2)
print(resu)
