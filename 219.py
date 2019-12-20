from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = set()
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
            dic.add(nums[i])
            if len(dic) > k:
                dic.remove(nums[i-k])
        return False


a = Solution()
in_para1 = [1, 2, 3,1]
in_para2 = 3
resu = a.containsNearbyDuplicate(in_para1, in_para2)
print(resu)
