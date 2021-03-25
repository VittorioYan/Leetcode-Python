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
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        size = len(nums)
        dp = [1]*size
        nums.sort()
        route = [[num] for num in nums]
        for i in range(size):
            for j in range(i):
                if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                    dp[i] = dp[j]+1
                    route[i] = route[j]+[nums[i]]
        return route[dp.index(max(dp))]



a = Solution()
in_para1 = [1,2,4,8]
in_para2 = [[0,1,2],[0,2,5]]
resu = a.largestDivisibleSubset(in_para1)
print(resu)
