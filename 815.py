from typing import List
from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==target:
            return 0
        n = len(routes)
        route_set = []
        memo = [n+1]*n
        q = deque([])
        end = set()
        for index,route in enumerate(routes):
            temp = set(route)
            if source in temp:
                q.append(index)
                memo[index] = 1
            if target in temp:
                end.add(index)
            route_set.append(temp)

        trace = [set() for _ in range(n)]

        for i in range(n-1):
            for j in range(i+1,n):
                cross = route_set[i] & route_set[j]
                if len(cross)>0:
                    trace[i].add(j)
                    trace[j].add(i)

        while q:
            cur = q.popleft()
            if cur in end:
                return memo[cur]
            for nex in list(trace[cur]):
                if memo[nex]>memo[cur]+1:
                    memo[nex]=memo[cur]+1
                    q.append(nex)
        return -1


a = Solution()
in_para1 = [[1,2,7],[3,6,7]]

in_para2 = [2,4]
resu = a.numBusesToDestination(in_para1,1,6)
print(resu)
