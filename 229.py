from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        maj_a = nums[0]
        maj_b = nums[0]
        count_a = 0
        count_b = 0
        for num in nums:
            if num == maj_a:
                count_a += 1
                continue
            if num == maj_b:
                count_b += 1
                continue
            if count_a == 0:
                maj_a = num
                count_a = 1
                continue
            if count_b == 0:
                maj_b = num
                count_b = 1
                continue
            count_b -= 1
            count_a -= 1
        count_a = 0
        count_b = 0
        for num in nums:
            if num == maj_a:
                count_a += 1
            elif num == maj_b:
                count_b += 1
        result = []
        if count_a > len(nums) // 3:
            result.append(maj_a)
        if count_b > len(nums) // 3:
            result.append(maj_b)
        return result


a = Solution()
in_para1 = [1, 1, 1, 2, 3, 4, 5, 6]
in_para2 = 9
resu = a.majorityElement(in_para1)
print(resu)
