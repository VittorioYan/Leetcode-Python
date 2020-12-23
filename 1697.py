from typing import List
import collections
import bisect

class UF:
    id=[]
    def __init__(self,n:int):
        self.id=[i for i in range(n)]
    
    def find(self,p):
        while p!=self.id[p]:
            p=self.id[p]
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
            self.id[idp]=idq
            return True


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList = sorted(edgeList,key=lambda x:x[2],reverse=True)
        for i in range(len(queries)):
            queries[i].append(i)
        queries = sorted(queries,key=lambda x:x[2],reverse=True)
        ans = [True]*len(queries)
        edge,query = edgeList.pop(),queries.pop()
        
        union_find = UF(n)
        
        while True:
            if edge[2]>=query[2] and not union_find.connect(query[0],query[1]):
                ans[query[3]]=False
                if not queries:
                    return ans
                else:
                    query = queries.pop()
                continue
            if union_find.connect(query[0],query[1]):
                # ans.append(True)
                if not queries:
                    return ans
                else:
                    query = queries.pop()
                continue
            union_find.union(edge[0],edge[1])
            if not edgeList:
                # for _ in range(len(queries)+1):
                #     ans.append(True)
                return ans
            else:
                edge = edgeList.pop()
            # if query[3]==15:
            #     print(union_find.id)
            #     pass
            


            
        
            

a = Solution()
in_para1 = [[7,9,72],[28,29,52],[23,14,14],[21,19,42],[17,16,19],[23,8,3],[14,28,22],[14,19,7],[25,3,59],[11,16,92],[18,12,79],[2,8,77],[24,7,82],[23,22,53],[15,26,69],[30,27,33],[0,23,49],[22,27,51],[6,29,63],[10,14,65],[16,28,95],[12,23,92],[22,7,68],[8,29,74],[7,30,38],[4,18,81],[0,21,28],[3,18,44],[16,24,78],[20,2,32],[8,3,18],[12,27,19],[18,5,42],[27,15,8],[2,29,48],[13,18,97],[16,6,73],[18,28,33],[17,30,67],[0,8,62],[22,21,30],[0,20,16],[1,0,20],[26,27,63],[4,25,96],[5,14,2],[8,21,92],[13,20,96]]
in_para2 = [[30,26,81],[26,13,74],[15,19,63],[25,3,41],[30,11,77],[28,19,66],[16,7,3],[22,20,33],[20,8,56],[20,17,10],[9,14,10],[30,5,5],[24,22,96],[2,15,61],[25,6,82],[22,6,62],[3,22,7],[27,18,98],[23,15,61],[17,22,74],[21,22,27],[11,26,70],[8,21,99],[7,21,4],[10,20,5],[17,25,23],[22,6,74],[14,30,47],[28,2,100],[15,19,53],[7,28,16],[25,13,17],[20,11,71],[27,23,43],[15,30,27],[1,9,41],[12,13,54],[0,23,55],[22,17,90],[13,4,72],[18,12,85],[8,16,44],[28,21,37],[28,21,16],[9,12,99],[22,14,49],[15,23,66],[28,27,97]]
resu = a.distanceLimitedPathsExist(31,in_para1,in_para2)
print(resu)
