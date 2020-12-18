from typing import List
import collections

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        def dp(i:int,j:int):
            if memo[i][j]!=0:
                return memo[i][j]
            if i==-1:
                return j+1
            if j==-1:
                return i+1
            if word1[i]==word2[j]:
                return dp(i-1,j-1)
            else:
                memo[i][j]=min(dp(i-1,j),dp(i-1,j-1),dp(i,j-1))+1
                return memo[i][j]
        return dp(len(word1)-1,len(word2)-1)


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         memo = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
#         for i in range(len(word1)+1):
#             memo[i][0] = i
#         for j in range(len(word2)+1):
#             memo[0][j] = j
#         for i in range(1,len(word1)+1):
#             for j in range(1,len(word2)+1):
#                 if word1[i-1]==word2[j-1]:
#                     memo[i][j] = memo[i-1][j-1]
#                     continue
#                 else:
#                     memo[i][j] = min(memo[i][j-1],memo[i-1][j-1],memo[i-1][j])+1
#         print(memo)
#         return memo[len(word1)][len(word2)]


# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         memo = [0]*(len(word2)+1) 
#         for i in range(len(word2)+1):
#             memo[i] = i
#         last = 0
#         for i in range(1,len(word1)+1):
#             last = i-1
#             memo[0] = i
#             for j in range(1,len(word2)+1):
#                 last_a = memo[j]
#                 if word1[i-1]==word2[j-1]:
#                     memo[j] = last
#                     last = last_a
#                     continue
#                 else:
#                     memo[j] = min(memo[j-1],memo[j],last)+1
#                 last = last_a
#         return memo[-1]

a = Solution()
in_para1 = "intention"
in_para2 = "execution"
resu = a.minDistance(in_para1,in_para2)
print(resu)
