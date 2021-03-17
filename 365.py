from typing import DefaultDict, List, Sequence
import collections
import bisect
from queue import Queue
import math
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == 0 or x + y == z
        return z % math.gcd(x, y) == 0

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        q = Queue()
        q.put(x)
        q.put(y)
        seen = set([0,x,y])
        if z in seen:
            return True
        if x*y*z==0:
            return False
        while q.qsize()>0:
            cur = q.get()
            tmp = cur
            while tmp<x:
                if tmp not in seen:
                    q.put(tmp)
                    seen.add(tmp)
                tmp+=y
            if tmp-x not in seen:
                q.put(tmp-x)
                seen.add(tmp-x)
            tmp = cur
            while tmp<y:
                if tmp not in seen:
                    q.put(tmp)
                    seen.add(tmp)
                tmp+=x
            if tmp-y not in seen:
                q.put(tmp-y)
                seen.add(tmp-y)
            if z in seen:
                return True
        return False

        

a = Solution()
in_para1 = 2
in_para2 = 6
resu = a.canMeasureWater(in_para1,in_para2,3)
print(resu)
