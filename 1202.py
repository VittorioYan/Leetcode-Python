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
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        size = len(s)
        sort_str = {}
        id = []
        uf = UF(size)

        for pair in pairs:
            uf.union(pair[0],pair[1])
        for i in range(size):
            idi = uf.find(i)
            id.append(idi)
            sort_str[idi] = sort_str.get(idi,[])+[s[i]]
        for val in sort_str.values():
            val.sort(reverse=True)
        ans = ''
        for i in range(size):
            ans+=sort_str[id[i]].pop()
        return ans
            


a = Solution()
in_para1 = "dcab"
in_para2 = [[0,3],[1,2],[0,2]]
resu = a.smallestStringWithSwaps(in_para1,in_para2)
print(resu)
