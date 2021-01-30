from typing import List
import collections
import bisect

class UF:
    id=[]
    size = []
    block = 0
    def __init__(self,n:int):
        self.id=[i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.block = n
    
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
                self.block-=1
            else:
                self.id[idq]=idp
                self.size[idp]+=self.size[idq]
                self.block-=1
            return True
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x:x[0],reverse=True)
        ufa,ufb = UF(n+1),UF(n+1)
        ans = 0
        for edge in edges:
            level,left,right = edge
            if level==3:
                if ufa.union(left,right):
                    ufb.union(left,right)
                else:
                    ans+=1
            if level==2:
                if not ufb.union(left,right):
                    ans +=1
            if level==1:
                if not ufa.union(left,right):
                    ans +=1
        if ufa.block!=2 or ufb.block!=2:
            return -1
        return ans
       

a = Solution()
in_para1 =  13
in_para2 =  [[1,1,2],[2,2,3],[2,3,4],[1,3,5],[3,2,6],[2,3,7],[3,7,8],[3,2,9],[2,4,10],[2,9,11],[1,2,12],[3,4,13],[2,2,7],[1,1,9],[1,2,13],[2,7,13],[3,2,3],[1,7,10],[2,8,11],[1,2,7],[2,1,9],[2,2,9],[1,5,6],[2,4,9],[1,7,8],[1,4,6],[1,4,9],[3,7,13],[2,2,8],[2,2,6],[1,1,10],[1,1,11],[2,5,10],[1,2,9],[2,1,2],[1,3,4],[3,6,8],[3,6,13],[1,3,8],[1,1,6],[3,3,9],[1,2,3],[1,11,13]]
resu = a.maxNumEdgesToRemove(in_para1,in_para2)
print(resu)
