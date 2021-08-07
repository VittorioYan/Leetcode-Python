from collections import defaultdict
from typing import Counter, List
import heapq
class Solution:
    def maximumTime(self, time: str) -> str:
        t = list(time)
        if t[-1]=='?':
            t[-1]='9'
        if t[-2]=='?':
            t[-2]='5'
        if t[0]=='?':
            if t[1]=='?':
                t[0]='2'
                t[1] = '3'
            else:
                if t[1]>'3':
                    t[0] = '1'
                else:
                    t[0] = '2'
        elif t[1]=='?':
            if t[0]=='2':
                t[1]='3'
            else:
                t[1] = '9'
        return ''.join(t)
        


a = Solution()
in_para1 = "2?:?0"
in_para2 = 3056
resu = a.maximumTime(in_para1)
print(resu)
