from typing import List
import collections
import bisect

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        def get_num(count:int,lis:list):
            if count==0:
                return 0
            return lis[count-1]
        size = len(cardPoints)
        prefix,suffix = [0]*size,[0]*size
        prefix[0] = cardPoints[0]
        suffix[0] = cardPoints[-1]
        for i in range(1,size):
            prefix[i] = prefix[i-1]+cardPoints[i]
            suffix[i] = suffix[i-1]+cardPoints[-i-1]
        ans = 0
        for i in range(k+1):
            ans = max(ans,get_num(i,prefix)+get_num(k-i,suffix))
        return ans

        
a = Solution()
in_para1 = [96,90,41,82,39,74,64,50,30]
in_para2 =8
resu = a.maxScore(in_para1,in_para2)
print(resu)
