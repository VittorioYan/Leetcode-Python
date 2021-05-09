from typing import List, Sequence
import collections
import bisect
from sortedcontainers import SortedList


class UF:
    id=[]
    size = []
    def __init__(self,n:int,chunk_size:int):
        self.id=[i for i in range(n)]
        self.size = [1 for _ in range(n)]
        self.chunk = 0
        self.chunk_size = chunk_size
    
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
                self.chunk-=self.size[idp]//self.chunk_size
                self.chunk-=self.size[idq]//self.chunk_size
                self.id[idp]=idq
                self.size[idq]+=self.size[idp]
                
                self.chunk+=self.size[idq]//self.chunk_size
            else:
                self.chunk-=self.size[idp]//self.chunk_size
                self.chunk-=self.size[idq]//self.chunk_size
                self.id[idq]=idp
                self.size[idp]+=self.size[idq]
                
                self.chunk+=self.size[idp]//self.chunk_size
            return True

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n<m*k:
            return -1
        bloom_index = sorted(list(range(n)),key=lambda i:bloomDay[i])
        if k==1:
            return bloomDay[bloom_index[m-1]]
        uf = UF(n,k)
        cur_bloom = set()
        for _,bloom in enumerate(bloom_index):
            if bloom-1 in cur_bloom:
                uf.union(bloom,bloom-1)
            if bloom+1 in cur_bloom:
                uf.union(bloom,bloom+1)
            if uf.chunk>=m:
                return bloomDay[bloom]
            cur_bloom.add(bloom)


a = Solution()
in_para1 = [7,7,7,7,12,7,7]
in_para2 = 10
resu = a.minDays(in_para1,2,3)
print(resu)
