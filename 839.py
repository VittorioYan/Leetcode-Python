from typing import List
import collections
import bisect

class UF:
    id=[]
    size = []
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
            self.block-=1
            if self.size[idp]<self.size[idq]:
                self.id[idp]=idq
                self.size[idq]+=self.size[idp]
            else:
                self.id[idq]=idp
                self.size[idp]+=self.size[idq]
            return True

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        uf = UF(n)
        def is_similar(s1:str,s2:str):
            diff = 0
            for i in range(len(s1)):
                if s1[i]!=s2[i]:
                    diff+=1
                    if diff>2:
                        return False
            return diff==0 or diff==2
        for i in range(n):
            for j in range(i+1,n):
                if is_similar(strs[i],strs[j]):
                    uf.union(i,j)
        return uf.block

            

a = Solution()
in_para1 =  ["omv","ovm"]
in_para2 = [[0,1,2],[0,2,5]]
resu = a.numSimilarGroups(in_para1)
print(resu)
