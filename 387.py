from typing import List
import collections
import bisect
class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        if not s:
            return -1
        dic = {}
        for i in range(n):
            if s[i] in dic:
                dic[s[i]] = n
            else:
                dic[s[i]] = i
        _min = min(dic.values())
        return _min if _min != n else -1
              

a = Solution()
in_para1 = ""
in_para2 = "execution"
resu = a.firstUniqChar(in_para1)
print(resu)
