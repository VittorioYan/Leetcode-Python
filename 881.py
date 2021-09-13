from typing import List
import collections
import bisect
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans =len(people) 
        people.sort()
        while people:
            cur = people.pop()
            if not people:
                break
            together = bisect.bisect_right(people,limit - cur)
            if together>0:
                people.pop(together-1)
                ans-=1
        return ans
            

a = Solution()
in_para1 =[1,2]
in_para2 = 3
resu = a.numRescueBoats(in_para1,in_para2)
print(resu)
