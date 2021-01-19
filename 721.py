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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accounts.sort()
        accounts.append([''])
        size = len(accounts)
        cur = 0
        def handle(acc:list):
            name = acc[0][0]
            ans,new = [],[]
            flag = True
            cur_union = set()
            ans.append(set(acc[0][1:]))
            for i in range(1,len(acc)):
                cur_union = set()
                for item in ans:
                    for account in acc[i][1:]:
                        if account in item:
                            cur_union |= item
                            flag = False
                            break
                    if flag:
                        new.append(item)
                    flag = True
                new.append(cur_union|set(acc[i][1:]))
                ans = new
                new = []

            return [[name]+sorted(list(x)) for x in ans]
        result = []        
        for i in range(1,size):
            if accounts[i][0]!=accounts[cur][0]:
                result += handle(accounts[cur:i])
                cur = i
        return result


a = Solution()
in_para1 = [["Celine","Celine5@m.co","Celine2@m.co","Celine20@m.co","Celine20@m.co","Celine1@m.co"],["Ethan","Ethan7@m.co","Ethan16@m.co","Ethan0@m.co","Ethan12@m.co","Ethan7@m.co"],["John","John20@m.co","John6@m.co","John20@m.co","John3@m.co","John16@m.co"],["Celine","Celine1@m.co","Celine2@m.co","Celine2@m.co","Celine2@m.co","Celine12@m.co"],["Hanzo","Hanzo9@m.co","Hanzo5@m.co","Hanzo17@m.co","Hanzo7@m.co","Hanzo9@m.co"],["Hanzo","Hanzo13@m.co","Hanzo10@m.co","Hanzo1@m.co","Hanzo2@m.co","Hanzo2@m.co"],["John","John3@m.co","John1@m.co","John5@m.co","John2@m.co","John20@m.co"],["Hanzo","Hanzo9@m.co","Hanzo3@m.co","Hanzo13@m.co","Hanzo0@m.co","Hanzo19@m.co"],["Fern","Fern12@m.co","Fern6@m.co","Fern18@m.co","Fern16@m.co","Fern16@m.co"],["Gabe","Gabe0@m.co","Gabe10@m.co","Gabe0@m.co","Gabe19@m.co","Gabe3@m.co"],["Alex","Alex12@m.co","Alex17@m.co","Alex6@m.co","Alex16@m.co","Alex1@m.co"],["Gabe","Gabe16@m.co","Gabe20@m.co","Gabe13@m.co","Gabe6@m.co","Gabe6@m.co"],["Kevin","Kevin9@m.co","Kevin6@m.co","Kevin7@m.co","Kevin18@m.co","Kevin3@m.co"],["John","John13@m.co","John13@m.co","John14@m.co","John16@m.co","John1@m.co"],["David","David15@m.co","David8@m.co","David3@m.co","David14@m.co","David15@m.co"],["Celine","Celine8@m.co","Celine4@m.co","Celine18@m.co","Celine17@m.co","Celine16@m.co"],["Alex","Alex2@m.co","Alex11@m.co","Alex11@m.co","Alex2@m.co","Alex12@m.co"],["Hanzo","Hanzo2@m.co","Hanzo9@m.co","Hanzo19@m.co","Hanzo10@m.co","Hanzo12@m.co"],["Isa","Isa16@m.co","Isa1@m.co","Isa1@m.co","Isa10@m.co","Isa12@m.co"],["Celine","Celine0@m.co","Celine6@m.co","Celine5@m.co","Celine1@m.co","Celine13@m.co"]]
in_para2 = [[0,3],[1,2],[0,2]]
resu = a.accountsMerge(in_para1)
print(resu)
