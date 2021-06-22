from typing import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int: 
        n1,n2 = len(matrix),len(matrix[0])
        k = min(k,n1*n2)
        _map = [[-1]*n2 for _ in range(n1)]
        _map[0][0] = 0
        heap = [[matrix[0][0],0,0]]
        i=0
        while i<k:
            ans,x,y = heapq.heappop(heap)
            i+=1
            _map[x][y] = 1
            if x+1<n1 and _map[x+1][y]<0:
                heapq.heappush(heap,[matrix[x+1][y],x+1,y])
                _map[x+1][y] = 0
            if y+1<n2 and _map[x][y+1]<0:
                heapq.heappush(heap,[matrix[x][y+1],x,y+1])
                _map[x][y+1] = 0
        return ans

        

a = Solution()
in_para1 = [[1,5,9],[10,11,13],[12,13,15]]
in_para2 =  8
resu = a.kthSmallest(in_para1,in_para2)
print(resu)
