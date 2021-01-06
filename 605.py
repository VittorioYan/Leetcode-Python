from typing import List
import collections
import bisect
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if (i-1<0 or flowerbed[i-1]==0) and (i+1>=len(flowerbed) or flowerbed[i+1]==0):
                    n-=1
                    flowerbed[i] = 1
                    if n<=0:
                        return True
        return False

            

a = Solution()
in_para1 =[0]
in_para2 = 1
resu = a.canPlaceFlowers(in_para1,in_para2)
print(resu)
