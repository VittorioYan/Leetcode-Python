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
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList = sorted(edgeList,key=lambda x:x[2],reverse=True)
        # for i in range(len(queries)):
        #     queries[i].append(i)
        # queries = sorted(queries,key=lambda x:x[2],reverse=True)
        queryidx = sorted(range(len(queries)), key = lambda i:queries[i][2], reverse = True)

        ans = [True]*len(queries)
        edge = edgeList.pop()
        index = queryidx.pop()
        query = queries[index]
        
        union_find = UF(n)
        
        while True:
            if union_find.connect(query[0],query[1]):
                if not queryidx:
                    return ans
                else:
                    index = queryidx.pop()
                    query = queries[index]
                continue

            if edge[2]>=query[2]:
                ans[index]=False
                if not queryidx:
                    return ans
                else:
                    index = queryidx.pop()
                    query = queries[index]
                continue
            
            union_find.union(edge[0],edge[1])
            if not edgeList:
                return ans
            else:
                edge = edgeList.pop()


            
        
            

a = Solution()
in_para1 = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
in_para2 = [[0,1,2],[0,2,5]]
resu = a.distanceLimitedPathsExist(5,in_para1,in_para2)
print(resu)
