from typing import List, Sequence
import collections
import bisect
class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for s in S:
            if not stack or stack[-1]!=s:
                stack.append(s)
            else:
                stack.pop()
        return ''.join(stack)

a = Solution()
in_para1 = "a"
in_para2 = 4
resu = a.removeDuplicates(in_para1)
print(resu)
