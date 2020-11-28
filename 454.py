from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count_ab = {}
        for a in A:
            for b in B:
                if a+b in count_ab:
                    count_ab[a+b] += 1
                else:
                    count_ab[a+b] = 1
        ans = 0
        for c in C:
            for d in D:
                if -c-d in count_ab:
                    ans+=count_ab[-c-d]
        return ans 


a = Solution()
in_para1 = [3, 6, 9, 1]
A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
A=[-1, -1]
B=[-1, 1]
C=[-1, 1]
D=[1, -1]
A = [0]
B = [0]
C = [0]
D = [0]
resu = a.fourSumCount(A, B, C, D)
print(resu)
