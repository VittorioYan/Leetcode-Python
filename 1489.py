from typing import List
import collections
import bisect

class UF:
    id=[]
    size = []
    max_size = 0
    def __init__(self,n:int):
        self.id=[i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.max_size = 0
    
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
                self.max_size = max(self.max_size,self.size[idq])
            else:
                self.id[idq]=idp
                self.size[idp]+=self.size[idq]
                self.max_size = max(self.max_size,self.size[idp])
            return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        size = len(edges)
        index = sorted(range(size),key=lambda i:edges[i][2])
        cirtical,non_cirtical = [],[]
        uf = UF(n)
        min_val = 0
        for i in index:
            left,right,weight = edges[i]
            if uf.union(left,right):
                min_val+= weight
        if uf.max_size<n:
            return [[],[]]
        for k in range(size):
            cur_edges = []
            cur_val = 0
            uf = UF(n)
            for i in index:
                if k==i:
                    continue
                left,right,weight = edges[i]
                if uf.union(left,right):
                    cur_val+= weight
            if uf.max_size!=n or cur_val!=min_val:
                cirtical.append(k)
            else:
                uf = UF(n)
                left,right,weight = edges[k]
                cur_val = weight
                uf.union(left,right)
                for i in index:
                    if k==i:
                        continue
                    left,right,weight = edges[i]
                    if uf.union(left,right):
                        cur_val+= weight
                if cur_val==min_val:
                    non_cirtical.append(k)
                
        return [cirtical,list(set(non_cirtical))]
        


a = Solution()
in_para1 =[[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
in_para2 = 4
resu = a.findCriticalAndPseudoCriticalEdges(in_para2,in_para1)
print(resu)
