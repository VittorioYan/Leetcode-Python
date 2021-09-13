from typing import List
import collections
import bisect
from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:
        stack_left = []
        stack_star = []
        for index,char in enumerate(s):
            if char=='(':
                stack_left.append(index)
            elif char=='*':
                stack_star.append(index)
            elif char==')':
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False
        j = len(stack_star)-1
        i= len(stack_left)-1
        while(i>=0):
            if j<0:
                return False
            if stack_left[i]>stack_star[j]:
                j-=1
            else:
                i-=1
                j-=1
        return True

a = Solution()
in_para1 ="("
in_para2 = 1
resu = a.checkValidString(in_para1)
print(resu)
