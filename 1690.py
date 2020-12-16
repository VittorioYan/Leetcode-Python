from typing import List

# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         lens = len(stones)
#         dp = [[-1] * (lens) for _ in range(lens)]
#         sums = [[0] * (lens) for _ in range(lens)]
#         for i in range(lens):
#             dp[i][i] = 0
#             sums[i][i] = stones[i]
#             for j in range(i+1,lens):
#                 sums[i][j] = sums[i][j-1]+stones[j]
        
#         def deep_search(start:int,end:int)->int:
#             if dp[start][end]!=-1:
#                 return dp[start][end]

#             left = deep_search(start+1,end)
#             right = deep_search(start,end-1)
#             sl = sums[start+1][end]
#             sr = sums[start][end-1]
#             dp[start][end]= max(sl-left,sr-right)
#             return dp[start][end]

#         return deep_search(0,lens-1)

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        length = len(stones)
        nums = [0]*length
        nums[0] = stones[0]
        for i in range(1,length):            
            nums[i]=nums[i-1]+stones[i] 
        dp=[0]*length       
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[j] - nums[i] - dp[j], nums[j-1]-(nums[i-1] if i>0 else 0) - dp[j - 1])
        return dp[length - 1] 


# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         lens = len(stones)
#         dp = [[0] * (lens) for _ in range(lens)]
#         sums = [[0] * (lens) for _ in range(lens)]
#         for i in range(lens):
#             dp[i][i] = 0
#             sums[i][i] = stones[i]
#             for j in range(i+1,lens):
#                 sums[i][j] = sums[i][j-1]+stones[j]
        
#         for i in range(1,lens):
#             for j in range(lens-i):
#                 left = sums[j][j+i-1]-dp[j][j+i-1]
#                 right =sums[j+1][j+i]- dp[j+1][j+i] 
#                 dp[j][j+i] = max(left,right)

#         return dp[0][lens-1]


a = Solution()
in_para1 = [5,3,1,4,2]
in_para2 = "dog cat cat fish"
resu = a.stoneGameVII(in_para1)
print(resu)
