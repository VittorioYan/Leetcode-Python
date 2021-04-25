from typing import List
import collections
import bisect
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        ans = 0
        dic = collections.Counter(answers)
        for key,val in dic.items():
            ans+= math.ceil(val/(key+1))*(key+1)
        return ans

a = Solution()
in_para1 = [10,10,10]
in_para2 = "def"
resu = a.numRabbits(in_para1)
print(resu)
