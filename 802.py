from typing import DefaultDict, List
import collections
from collections import deque
import bisect
import heapq

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(poi:int,searched:set):
            if flag[poi]==1:
                return True
            if flag[poi]==-1:
                return False
            searched.add(poi)
            cur = True
            for ne in graph[poi]:
                if ne in searched:
                    cur = False
                    break
                cur = cur and dfs(ne,searched)
            if cur==True:
                flag[poi] = 1
            else:
                flag[poi] = -1
            searched.remove(poi)
            return cur

        n = len(graph)
        flag = [0]*n
        for i in range(n):
            dfs(i,set())
        return [i for i in range(n) if flag[i]==1]
        

            


a = Solution()
in_para1= [[1,2,3,4],[1,2],[3,4],[0,4],[]]
in_para2=[[0,2,2],[4,2,4],[2,13,1000000000]]
resu = a.eventualSafeNodes(in_para1)

print(resu)
