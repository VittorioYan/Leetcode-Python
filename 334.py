from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        import sys
        first_min = sys.maxsize
        second_min = sys.maxsize
        for num in nums:
            if num > second_min:
                return True
            if first_min < num < second_min:
                second_min = num
            if num < first_min:
                first_min = num
        return False


a = Solution()
in_para1 = [1, 0,0,0, 2]
in_para2 = 9
resu = a.increasingTriplet(in_para1)
print(resu)
