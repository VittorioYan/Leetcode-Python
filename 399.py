from typing import List, Sequence
import collections
import bisect

class node:
    def __init__(self,name) -> None:
        self.name:str = name
        self.next:dict = {}

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        roads = {}
        for i in range(len(equations)):
            roads[equations[i][0]] = roads.get(equations[i][0],node(equations[i][0]))
            roads[equations[i][1]] = roads.get(equations[i][1],node(equations[i][0]))
            roads[equations[i][0]].next[equations[i][1]] = values[i]
            roads[equations[i][1]].next[equations[i][0]] = 1/values[i]
        ans = []
        def dfs(now,aim):
            nonlocal flag
            if now==aim:
                return 1
            if now in flag:
                return -1
            flag[now] = True
            for item in roads[now].next.items():
                u = dfs(item[0],aim)
                if u>0:
                    return item[1]*u
            return -1
        for query in queries:
            flag = {}
            if query[0] in roads and query[1] in roads:
                ans.append(dfs(query[0],query[1]))
            else:
                ans.append(-1)
                
        return ans



a = Solution()
in_para1 =  [["a","b"]]
in_para2 =  [0.5]
resu = a.calcEquation(in_para1,in_para2,  [["a","b"],["b","a"],["a","c"],["x","y"]])
print(resu)
