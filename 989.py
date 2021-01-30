from typing import List
import heapq

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        for i in range(len(A)-1,-1,-1):
            if K:
                cur = A[i] +K
                A[i] = cur%10
                K = cur//10
        if K==0:
            return A
        else:
            return [int(x) for x in str(K)]+A

a = Solution()
in_para1 = [2,1,5]
in_para2 = 806
resu = a.addToArrayForm(in_para1,in_para2)
print(resu)
