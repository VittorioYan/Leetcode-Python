from typing import DefaultDict, List
import collections
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        size = len(s)
        count = collections.Counter(s)
        sort_count = sorted(count.items(),key=lambda i:i[1])
        if sort_count[0][1]>=k:
            return size
        
        aim = sort_count[0][0]
        return max(self.longestSubstring(t,k) for t in s.split(aim))


                

a = Solution()
in_para1 = "ababbc"
in_para2 = 2
resu = a.longestSubstring(in_para1,in_para2)
print(resu)
