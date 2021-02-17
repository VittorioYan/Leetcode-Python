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
    def minSwapsCouples(self, row: List[int]) -> int:
        def couple(a:int):
            if a%2==0:
                return a+1
            return a-1
        def find_couple(seats:list,cur:int):
            a = couple(cur)
            for index,seat in enumerate(seats):
                if a in seat:
                    return index

        def find_circle(uf:UF,seats:list,index:int):
            seat = seats[index]
            uf.union(index,find_couple(seats,seat[0]))
            uf.union(index,find_couple(seats,seat[1]))
            

        seats = []
        for i in range(len(row)//2):
            seats.append((row[2*i],row[2*i+1]))
        size = len(seats)
        uf = UF(size)
        for index,_ in enumerate(seats):
            find_circle(uf,seats,index)
        return size-uf.block
            
            
a = Solution()
in_para1 =  [3, 2, 0, 1]
in_para2 = [2]
resu = a.minSwapsCouples(in_para1)
print(resu)
