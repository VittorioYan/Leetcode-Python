from typing import List
import bisect
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def cost(a,b):
            return abs(ord(a)-ord(b))
        length = len(s)
        l,r = 0,0
        ans = 0
        cur_cost = 0
        while r<length:
            cur_cost += cost(s[r],t[r])
            while l<=r:
                if cur_cost>maxCost:
                    cur_cost-=cost(s[l],t[l])
                    l+=1
                else:
                    ans = max(r-l+1,ans)
                    break
            r+=1
        return ans

a = Solution()
in_para1 = "abcd"
in_para2 = "acde"
resu = a.equalSubstring(in_para1,in_para2,0)
print(resu)
