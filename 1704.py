from typing import List
# import sys
import heapq
import collections
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s)//2
        a ,b = collections.Counter(s[:half]),collections.Counter(s[half:])
        aim = 'aeiouAEIOU'
        ans = 0
        for item in aim:
            ans+=a.get(item,0)-b.get(item,0)
        return ans==0

a = Solution()
in_para1 = "ok"
in_para2 = ["abcddefg"]
resu = a.halvesAreAlike(in_para1)
print(resu)
