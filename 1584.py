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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def val(poi1:list,poi2:list):
            return abs(poi1[0]-poi2[0])+abs(poi1[1]-poi2[1])
        path = []
        size = len(points)
        for i in range(size):
            for j in range(i+1,size):
                path.append((val(points[i],points[j]),i,j))
        path.sort(key=lambda x:x[0])
        uf = UF(size)
        res = 0
        count = 0
        for p in path:
            if count>=size-1:
                break
            v,i,j = p
            if uf.union(i,j):
                res+=v
                count+=1
        return res


a = Solution()
in_para1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
in_para2 = [[0,3],[1,2],[0,2]]
resu = a.minCostConnectPoints(in_para1)
print(resu)
