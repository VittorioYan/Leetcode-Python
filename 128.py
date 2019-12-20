from typing import List

class Solution:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.num_dict = {}

    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        for num in nums:
            self.add_new_num(num)

        print(self.num_dict)
        return max(self.num_dict.values())

    def add_new_num(self, num):
        if num in self.num_dict:
            return
        else:
            self.num_dict[num] = 1
        if num-1 in self.num_dict:
            self.combine(num-1, num)
        if num+1 in self.num_dict:
            self.combine(num, num+1)

    def combine(self, seq_left, seq_right):
        left_len = self.num_dict[seq_left]
        right_len = self.num_dict[seq_right]
        seq_len = left_len + right_len
        self.num_dict[seq_left] = seq_len
        self.num_dict[seq_right] = seq_len
        self.num_dict[seq_left - left_len + 1] = seq_len
        self.num_dict[seq_right + right_len - 1] = seq_len



a = Solution()
res = a.longestConsecutive(nums=[100, 4, 200, 1, 3, 2,5,7])
print(res)