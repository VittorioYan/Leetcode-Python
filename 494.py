from typing import List
# class Solution:
#     def findTargetSumWays(self, nums: List[int], S: int) -> int:
#         count = {0:1}
#         for num in nums:
#             cur_count = {}
#             for key,value in count.items():
#                 cur_count[key+num] = cur_count[key+num]+value if key+num in cur_count else value
#                 cur_count[key-num] = cur_count[key-num]+value if key-num in cur_count else value
#             count = cur_count
#         return count.get(S,0)

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        _sum = sum(nums)
        if _sum<S or (S+_sum)%2==1:
            return 0
        target = int((S+_sum)/2)

        dp = [0]*(target+1)
        dp[0] = 1
            
        for i in range(1,len(nums)+1):
            for j in range(target,-1,-1):
                dp[j] = dp[j]+(dp[j-nums[i-1]] if j>=nums[i-1] else 0)
        return dp[target]

        



a = Solution()
# in_para1 = [0,0,0,0,0,0,0,0,1]
in_para1 = [1,1,1,1,1]
in_para2 = 1
resu = a.findTargetSumWays(in_para1,in_para2)
print(resu)
