from typing import List
# import sys
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        def reverse(input:int,times:int):
            if times%2==0:
                return input
            else:
                return abs(input-1)
        size = len(A)
        diff = [0]*(size+1)
        cur = 0
        ans = 0
        for index,num in enumerate(A):
            if reverse(num,cur+diff[index])==0:
                if index+K>size:
                    return -1
                ans+=1
                diff[index]+=1
                diff[index+K]+=1
            cur+=diff[index]

        return ans


a = Solution()
in_para1 = [0,1,0]
in_para2 = 1
resu = a.minKBitFlips(in_para1,in_para2)
print(resu)
