from typing import List
import collections
import bisect
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9+7
        pre = {'0l0a':1,'0l1a':0,'1l0a':0,'1l1a':0,'2l0a':0,'2l1a':0}
        for _ in range(n):
            cur = {}
            cur['0l0a'] = (pre['0l0a']+pre['1l0a']+pre['2l0a'])%MOD
            cur['0l1a'] = sum(pre.values())%MOD
            cur['1l0a'] = pre['0l0a']%MOD
            cur['1l1a'] = pre['0l1a']%MOD
            cur['2l0a'] = pre['1l0a']%MOD
            cur['2l1a'] = pre['1l1a']%MOD
            pre = cur
        return sum(pre.values())%MOD




a = Solution()
in_para1 = 3
in_para2 = [[0, 1], [2, 3]]
resu = a.checkRecord(in_para1)
print(resu)
