from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]
        def dfs(nums, i, j):
            if j <= i:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if j - i == 1:
                dp[i][j] = nums[i] * nums[i - 1] * nums[j]
                return dp[i][j]
            max_point = 0
            for k in range(i, j):
                cur_point = nums[k] * nums[i - 1] * nums[j]
                max_point = max(max_point, cur_point + dfs(nums, i, k) + dfs(nums, k + 1, j))
            dp[i][j] = max_point
            return dp[i][j]

        return dfs(nums, 1, n - 1)
# 回溯递归在深度很大时超时
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[-1]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]
        def dfs(i,j):
            if dp[i][j]>=0:
                return dp[i][j] 
            cur = 0
            for k in range(i+1,j):
                cur = max(cur,dfs(i,k)+nums[k]*nums[i]*nums[j]+dfs(k,j))
            dp[i][j] = cur
            return dp[i][j]
        return dfs(0,n-1)

# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:

#         #nums首尾添加1，方便处理边界情况
#         nums.insert(0,1)
#         nums.insert(len(nums),1)

#         store = [[0]*(len(nums)) for i in range(len(nums))]

#         def range_best(i,j):
#             m = 0 
#             #k是(i,j)区间内最后一个被戳的气球
#             for k in range(i+1,j): #k取值在(i,j)开区间中
#                 #以下都是开区间(i,k), (k,j)
#                 left = store[i][k]
#                 right = store[k][j]
#                 a = left + nums[i]*nums[k]*nums[j] + right
#                 if a > m:
#                     m = a
#             store[i][j] = m

#         #对每一个区间长度进行循环
#         for n in range(2,len(nums)): #区间长度 #长度从3开始，n从2开始
#             #开区间长度会从3一直到len(nums)
#             #因为这里取的是range，所以最后一个数字是len(nums)-1

#             #对于每一个区间长度，循环区间开头的i
#             for i in range(0,len(nums)-n): #i+n = len(nums)-1

#                 #计算这个区间的最多金币
#                 range_best(i,i+n)

#         return store[0][len(nums)-1]



a = Solution()
in_para1 = [5]
in_para2 = 9
resu = a.maxCoins(in_para1)
print(resu)
