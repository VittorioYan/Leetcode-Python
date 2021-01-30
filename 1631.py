from typing import List, Sequence, Tuple
import collections
import bisect

# 暴搜DFS超时
# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#         m,n = len(heights),len(heights[0])
#         dp = [[1000000]*n for _ in range(m)]
#         def dfs(point):
#             i,j  = point
#             if i>0:
#                 mid = max(abs(heights[i][j]-heights[i-1][j]),dp[i][j])
#                 if dp[i-1][j]>mid:
#                     dp[i-1][j] = mid
#                     dfs((i-1,j))
#             if j>0:
#                 mid = max(abs(heights[i][j]-heights[i][j-1]),dp[i][j])
#                 if dp[i][j-1]>mid:
#                     dp[i][j-1] = mid
#                     dfs((i,j-1))
#             if i<m-1:
#                 mid = max(abs(heights[i][j]-heights[i+1][j]),dp[i][j])
#                 if dp[i+1][j]>mid:
#                     dp[i+1][j] = mid
#                     dfs((i+1,j))
#             if j<n-1:
#                 mid = max(abs(heights[i][j]-heights[i][j+1]),dp[i][j])
#                 if dp[i][j+1]>mid:
#                     dp[i][j+1] = mid
#                     dfs((i,j+1))
#         dp[0][0] = 0
#         dfs((0,0))
#         return dp[-1][-1]

# BFS
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m,n = len(heights),len(heights[0])
        dp = [[1000000]*n for _ in range(m)]
        def bfs(queue:list,q_set:set):
            if not queue:
                return
            q_set.remove(queue[0])
            i,j  = queue.pop(0)
            if i>0:
                mid = max(abs(heights[i][j]-heights[i-1][j]),dp[i][j])
                if dp[i-1][j]>mid:
                    dp[i-1][j] = mid
                    next = (i-1,j)
                    if next not in q_set:
                        queue.append(next)
                        q_set.add(next)
                    
            if j>0:
                mid = max(abs(heights[i][j]-heights[i][j-1]),dp[i][j])
                if dp[i][j-1]>mid:
                    dp[i][j-1] = mid
                    next = (i,j-1)
                    if next not in q_set:
                        queue.append(next)
                        q_set.add(next)
            if i<m-1:
                mid = max(abs(heights[i][j]-heights[i+1][j]),dp[i][j])
                if dp[i+1][j]>mid:
                    dp[i+1][j] = mid
                    next = (i+1,j)
                    if next not in q_set:
                        queue.append(next)
                        q_set.add(next)
            if j<n-1:
                mid = max(abs(heights[i][j]-heights[i][j+1]),dp[i][j])
                if dp[i][j+1]>mid:
                    dp[i][j+1] = mid
                    next = (i,j+1)
                    if next not in q_set:
                        queue.append(next)
                        q_set.add(next)
            bfs(queue,q_set)
        dp[0][0] = 0
        queue = [(0,0)]
        q_set = set(queue)
        bfs(queue=queue,q_set=q_set)
        return dp[-1][-1]


a = Solution()
in_para1 = [[1]]
in_para2 = "execution"
resu = a.minimumEffortPath(in_para1)
print(resu)
