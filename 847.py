from typing import DefaultDict, List
import collections
from collections import deque
import bisect
import heapq

class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # def Floyd(graph:List[List[int]]):
        #     n = len(graph)
        #     dist = [[float('inf')]*n for _ in range(n)]
        #     for index,g in enumerate(graph):
        #         for a in g:
        #             dist[index][a] = 1
        #             dist[a][index] = 1
        #     for k in range(n):
        #         for i in range(n):
        #             for j in range(n):
        #                 if dist[i][j]>dist[i][k]+dist[k][j]:
        #                     dist[i][j]=dist[i][k]+dist[k][j]
        #     return dist
        n = len(graph)
        base = '0'*n
        q = deque([])
        for i in range(n):
            q.append((i,base[:i]+'1'+base[i+1:],0))
        flag = set()
        def bfs(pos,mask,dist):
            if (pos,mask) in flag:
                return
            flag.add((pos,mask))
            if mask == '1'*n:
                raise Exception(dist)
            for ne in graph[pos]:
                q.append((ne,mask[:ne]+'1'+mask[ne+1:],dist+1))
        
        try:
            while q:
                cur = q.popleft()
                bfs(*cur)
        except Exception as e:
            return e.args[0]




a = Solution()
in_para1= [[1],[0,2,4],[1,3,4],[2],[1,2]]
in_para2=[[0,2,2],[4,2,4],[2,13,1000000000]]
resu = a.shortestPathLength(in_para1)

print(resu)
