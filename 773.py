from typing import DefaultDict, List
import collections
from collections import Counter,deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def exchange_char(s:str,i1:int,i2:int)->str:
            l = min(i1,i2)
            r = max(i1,i2)
            return s[:l]+s[r]+s[l+1:r]+s[l]+s[r+1:]

        def find_state(state:str)->list:
            change = {0:[1,3],1:[0,2,4],2:[1,5],3:[0,4],4:[3,1,5],5:[2,4]}
            index_0 = state.index('0')
            res = []
            for i in change[index_0]:
                res.append(exchange_char(state,index_0,i))
            return res

        def update(q:deque,map1,map2):
            cur = q.popleft()
            next_state = find_state(cur)
            for nex in next_state:
                if nex in map2:
                    return map2[nex]+map1[cur]+1
                if nex in map1:
                    continue
                else:
                    map1[nex] = map1[cur]+1
                    q.append(nex)
            return -1
                
        start = ''
        for i in board:
            for j in i:
                start+=str(j)
        end = '123450'
        dp1,dp2 = {start:0},{end:0}
        q1,q2 = deque([start]),deque([end])
        if start==end:
            return 0
        while q1 and q2:
            if len(q1)>len(q2):
                ans = update(q2,dp2,dp1)
            else:
                ans = update(q1,dp1,dp2)
            if ans!=-1:
                return ans
        return -1
        
        


a = Solution()
in_para1 = [[1,2,3],[5,4,0]]
in_para2 = 2
resu = a.slidingPuzzle(in_para1)
print(resu)
