from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        def add_result(index1,index2,ans):
            ans.append([nums1[index1],nums2[index2]])
        n1,n2 = len(nums1),len(nums2)
        k = min(k,n1*n2)
        _map = [[-1]*n2 for _ in range(n1)]
        heap = [[nums1[0]+nums2[0],0,0]]
        _map[0][0] = 0
        i=0
        ans = []
        while i<k:
            _,x,y = heapq.heappop(heap)
            add_result(x,y,ans)
            i+=1
            _map[x][y] = 1
            if x+1<n1 and _map[x+1][y]<0:
                heapq.heappush(heap,[nums1[x+1]+nums2[y],x+1,y])
                _map[x+1][y] = 0
            if y+1<n2 and _map[x][y+1]<0:
                heapq.heappush(heap,[nums1[x]+nums2[y+1],x,y+1])
                _map[x][y+1] = 0
        return ans

        

a = Solution()
in_para1 = [1,1,2]
in_para2 = [1,2,3]
resu = a.kSmallestPairs(in_para1,in_para2,10)
print(resu)
