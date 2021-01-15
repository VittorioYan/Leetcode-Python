from typing import List
import collections
import bisect

class UF:
    id=[]
    size = []
    def __init__(self,n:int):
        self.id=[i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self,p):
        stk = []
        while p!=self.id[p]:
            stk.append(p)
            p=self.id[p]
        for item in stk:
            self.id[item] = p
        return p

    def connect(self,p,q):
        if self.find(p)!=self.find(q):
            return False
        else:
            return True

    def union(self,p,q):
        idp = self.find(p)
        idq = self.find(q)
        if idp==idq:
            return False
        else:
            if self.size[idp]<self.size[idq]:
                self.id[idp]=idq
                self.size[idq]+=self.size[idp]
            else:
                self.id[idq]=idp
                self.size[idp]+=self.size[idq]
            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        size = len(edges)
        uf = UF(size+1)
        ans = []
        for edge in edges:
            if not uf.union(edge[0],edge[1]):
                ans = edge
        return ans
            


a = Solution()
in_para1 = [[1,2], [2,3], [3,4], [1,4], [1,5]]
in_para2 = [[0,3],[1,2],[0,2]]
resu = a.findRedundantConnection(in_para1)
print(resu)
