from typing import List, Sequence
import collections
import bisect

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1]+[-1]*target
        nums.sort()
        def dfs(target:int):
            cur_ans = 0
            if dp[target]>=0:
                return dp[target]
            for num in nums:
                if num<=target:
                    cur_ans +=dfs(target-num)
            dp[target] = cur_ans
            return cur_ans
        return dfs(target)


a = Solution()
in_para1 = [4,2,1]
in_para2 = 32
resu = a.combinationSum4(in_para1,in_para2)
print(resu)
