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
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        uf = UF(n)
        block,circle_edge = n,0
        for connection in connections:
            left,right = connection
            if uf.union(left,right):
                block-=1
            else:
                circle_edge+=1
        if block-1>circle_edge:
            return -1
        else:
            return block-1

        
a = Solution()
in_para1 =  [[0,1],[0,2],[3,4],[2,3]]
in_para2 = [[0,1,2],[0,2,5]]
resu = a.makeConnected(5,in_para1)
print(resu)
