from typing import Counter, List
import collections
import bisect
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0,1]
        if num<=1:
            return ans[:num+1]
        max_2 = 1
        for i in range(2,num+1):
            if i & (i-1)==0:
                ans.append(1)
                max_2 = i
            else:
                ans.append(1+ans[i-max_2])
        return ans

        
a = Solution()
in_para1 =5
in_para2 = [0]
resu = a.countBits(in_para1)
print(resu)
