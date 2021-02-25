from typing import Counter, List
import collections
import bisect
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        def reverse_row(aim:list):
            size = len(aim)
            for i in range((size+1)//2):
                tmp = 1-aim[i]
                aim[i] = 1-aim[-i-1]
                aim[-i-1] = tmp
        for a in A:
            reverse_row(a)
        return A

a = Solution()
in_para1 =[[1,1,0],[1,0,1],[0,0,0]]
in_para2 = [0]
resu = a.flipAndInvertImage(in_para1)
print(resu)
