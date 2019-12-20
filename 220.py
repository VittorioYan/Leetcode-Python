from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) <= 1:
            return False
        if t < 0 or k <= 0:
            return False
        from collections import OrderedDict
        dic = OrderedDict()
        for i in range(len(nums)):
            cur_id = nums[i] // (t + 1)
            if cur_id in dic.keys():
                return True
            if cur_id - 1 in dic and abs(nums[i] - dic[cur_id - 1]) <= t:
                return True
            if cur_id + 1 in dic and abs(nums[i] - dic[cur_id + 1]) <= t:
                return True
            dic[cur_id] = nums[i]
            if len(dic) > k:
                dic.popitem(0)
        return False



a = Solution()
in_para1 = [1,5,9,1,5,9]

in_para2 = 2
resu = a.containsNearbyAlmostDuplicate(in_para1, in_para2, 3)
print(resu)
