from typing import List
import sys

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        now_max = 0
        max_index = 0
        result = []

        def helper(numss):
            he_max = -sys.maxsize
            he_index = 0
            for i in range(len(numss)):
                if numss[i] > he_max:
                    he_max = numss[i]
                    he_index = i
            return he_max, he_index

        for i in range(len(nums)):
            if nums[i] > now_max:
                now_max = nums[i]
                max_index = i
            if i - max_index >= k:
                now_max, max_index = helper(nums[i - k+1:i+1])
            if i >= k-1:
                result.append(now_max)

        return result

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = []
        res = []
        for i in range(len(nums)):
            # 把这个队列索引号控制在k内
            if queue and i - queue[0] + 1 > k:
                queue.pop(0)
            # 维护一个单调递减的数列
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            queue.append(i)
            if i - k + 1 >= 0:
                res.append(nums[queue[0]])
        return res



a = Solution()
in_para1 = [1,3,-1,-3,5,3,6,7]
in_para2 = 3
resu = a.maxSlidingWindow(in_para1, in_para2)
print(resu)
