from typing import List
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = -(10 ** 9 + 7)
        for i in range(len(nums) - 1,-1,-1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = max(k,stack.pop())
            stack.append(nums[i])
        return False

a = Solution()
in_para1 = [3,1,2,4]
in_para2 = [1,0]
resu = a.find132pattern(in_para1)
print(resu)
