from typing import List
import collections
import bisect
class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.index('LLL')<0 and len(s.split('A'))>=2
            



a = Solution()
in_para1 = "PPALLP"
in_para2 = [[0, 1], [2, 3]]
resu = a.checkRecord(in_para1)
print(resu)
