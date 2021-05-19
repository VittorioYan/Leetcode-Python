from typing import List
import collections
import bisect
import heapq
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m,n = len(matrix),len(matrix[0])
        ans_mat = [[0]*n for _ in range(m)]
        heap = []
        for i in range(m):
            for j in range(n):
                left = ans_mat[i][j-1] if j>0 else 0
                up =  ans_mat[i-1][j] if i>0 else 0
                leftup = ans_mat[i-1][j-1] if i>0 and j>0 else 0
                ans_mat[i][j] = left^up^leftup^matrix[i][j]
                if len(heap)<k:
                    heapq.heappush(heap,ans_mat[i][j])
                else:
                    if heap[0]<ans_mat[i][j]:
                        heapq.heapreplace(heap,ans_mat[i][j])
        return heap[0]
a = Solution()
in_para1 = [[5,2],[1,6]]
in_para2 = 3
resu = a.kthLargestValue(in_para1,in_para2)
print(resu)
