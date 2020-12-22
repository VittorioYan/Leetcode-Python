from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        _set = set()
        _set.add(nums[0])
        i,j = 0,1
        ans = 0
        while j<len(nums):
            if nums[j] in _set:
                ans = max(ans,sum(_set))
                while i<j:
                    _set.remove(nums[i])
                    i += 1
                    if nums[i-1]==nums[j]:
                        break
            _set.add(nums[j])
            j+=1
        return max(ans,sum(_set))

a = Solution()
in_para1 = [5,2,1,2,5,4,2,1,6,2,5]
in_para2 = "execution"
resu = a.maximumUniqueSubarray(in_para1)
print(resu)
