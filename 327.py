from typing import List
import bisect


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        ans = 0
        queue = []
        for pre in prefix[::-1]:
            i, j = pre + lower, pre + upper
            l = bisect.bisect_left(queue, i)
            r = bisect.bisect_right(queue, j)
            ans += r - l
            bisect.insort(queue, pre)
        return ans


a = Solution()
in_para1 = [-2, 5, -1]
in_para2 = 9
resu = a.countRangeSum(in_para1, -2, 2)
print(resu)
