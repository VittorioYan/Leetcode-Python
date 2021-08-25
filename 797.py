from typing import List
import collections
import bisect
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        ans = []
        def dfs(cur:int,trace:list):
            if cur == n-1:
                ans.append(trace.copy())
                return
            for nex in graph[cur]:
                cur_trace = trace.copy()
                cur_trace.append(nex)
                dfs(nex,cur_trace)
                cur_trace.pop()

            
        dfs(0,[0])
        return ans



a = Solution()
in_para1 =[[1],[]]
in_para2 = [[0, 1], [2, 3]]
resu = a.allPathsSourceTarget(in_para1)
print(resu)
