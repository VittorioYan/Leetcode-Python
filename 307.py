from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0]
        self.nums = nums
        self.change = {}
        for num in nums:
            self.dp.append(self.dp[-1] + num)

    def update(self, i: int, val: int) -> None:
        self.change[i] = val - self.nums[i]

    def sumRange(self, i: int, j: int) -> int:
        change_num = 0
        for key in self.change.keys():
            if i <= key <= j:
                change_num += self.change[key]
        return self.dp[j + 1] - self.dp[i] + change_num


# Your NumArray object will be instantiated and called as such:
nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, 2)
print(obj.sumRange(0, 2))
