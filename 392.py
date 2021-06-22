from typing import Counter, List, Text
import collections
import bisect
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        position =collections.defaultdict(list)
        for index,item in enumerate(t):
            position[item].append(index)
        next_pos = -1
        for item in s:
            temp = bisect.bisect_right(position[item],next_pos)
            if temp>=len(position[item]):
                return False
            next_pos = position[item][temp]
        return True


a = Solution()
in_para1 ="aaaabc"
in_para2 = "aahabagdc"
resu = a.isSubsequence(in_para1,in_para2)
print(resu)
