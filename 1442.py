from typing import List
import collections
import bisect

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)
        dic = [[0]*n for _ in range(n)]
        for i in range(n):
            dic[i][i] = arr[i]
            for j in range(i+1,n):
                dic[i][j] = dic[i][j-1]^arr[j]

        for i in range(n):
            for k in range(i+1,n):
                for j in range(i+1,k+1):
                    if dic[i][j-1]==dic[j][k]:
                        print(i,j,k)
                        ans+=1
        return ans

            
a = Solution()
in_para1 = [2,3,1,6,7]
in_para2 = 4
resu = a.countTriplets(in_para1)
print(resu)
