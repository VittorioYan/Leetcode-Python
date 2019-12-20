from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0]
        for num in nums:
            self.dp.append(self.dp[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
i = 0
j = 5
obj = NumArray(nums)
param_1 = obj.sumRange(i, j)
print(param_1)
