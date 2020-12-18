from typing import List
import collections
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_a = collections.Counter(s)
        for item in list(t):
            if not count_a[item] or count_a[item]==0:
                return item
            count_a[item]-=1



a = Solution()
in_para1 = "ae"
in_para2 = "aea"
resu = a.findTheDifference(in_para1,in_para2)
print(resu)
