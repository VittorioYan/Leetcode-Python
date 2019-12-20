from typing import List


class Solution:
    def insert(self, nums: list, left: int, right: int, in_num: int):
        n = right - left
        if n == 1:
            if nums[left] >= in_num:
                return left
            else:
                return left + 1

        flag = left + n // 2
        if nums[flag] >= in_num:
            return self.insert(nums, left, flag, in_num)
        else:
            return self.insert(nums, flag, right, in_num)

    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [0]
        ans = [0]
        sorted_num = [nums[-1]]
        for i in range(n - 2, -1, -1):
            insert_index = self.insert(sorted_num, 0, len(sorted_num), nums[i])
            ans.append(insert_index)
            sorted_num = sorted_num[:insert_index]+[nums[i]]+sorted_num[insert_index:]
        ans.reverse()
        return ans


a = Solution()
in_para1 = [5,7,1,3,4,6,3]
in_para2 = [1, 2, 5, 6]
resu = a.countSmaller(in_para1)
print(resu)
