from typing import List
import collections
import bisect
import random

class Solution:

    def __init__(self, w: List[int]):
        self.l = []
        
        for item in w:
            self.l.append(item+self.l[-1])
        self.total = self.l[-1]

    def pickIndex(self) -> int:
        cur = random.randint(1,self.total)
        return bisect.bisect_left(self.l,cur)



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
            

a = Solution()
in_para1 =[1,2]
in_para2 = 3
resu = a.numRescueBoats(in_para1,in_para2)
print(resu)
