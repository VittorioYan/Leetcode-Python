from typing import List
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)
        aim = N*N
        dp = [aim+1]*(N*N+1)
        route = [-1]
        flag = True
        for i in range(N-1,-1,-1):
            if flag:
                for j in range(N):
                    route.append(board[i][j])   
            else:
                for j in range(N-1,-1,-1):
                    route.append(board[i][j])
            flag= not flag
        
        dp[1] = 0
        q = deque([1])
        while q:
            cur = q.popleft()
            if cur==aim:
                continue
            no_jump = 0
            # if route[cur]!=-1:
            #     if dp[route[cur]] > dp[cur]+1:
            #             dp[route[cur]] = dp[cur]+1
            #             q.append(route[cur])
            #     continue
            for i in range(1,7):
                if cur+i==aim:
                    dp[cur+i] = min(dp[cur]+1,dp[-1])
                    break
                if route[cur+i] != -1:
                    if dp[route[cur+i]] > dp[cur]+1:
                        dp[route[cur+i]] = dp[cur]+1
                        q.append(route[cur+i])
                else:
                    temp = cur+i
                    if dp[temp] > dp[cur]+1:
                        dp[temp] = dp[cur]+1
                        no_jump = temp
            if no_jump:
                q.append(no_jump)
        if dp[-1]!=aim+1:
            return dp[-1]
        else:
            return -1



a = Solution()
in_para1 =[[-1,-1,19,10,-1],[2,-1,-1,6,-1],[-1,17,-1,19,-1],[25,-1,20,-1,-1],[-1,-1,-1,-1,15]]

in_para2 = [2,4]
resu = a.snakesAndLadders(in_para1)
print(resu)
