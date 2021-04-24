from typing import DefaultDict, List
import collections
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        size = len(A)
        if size<3:
            return True
        flag = 0
        for i in range(1,size):
            if A[i] - A[i-1]<0:
                if flag==1:
                    return False
                flag = -1
            if A[i] - A[i-1]>0:
                if flag==-1:
                    return False
                flag = 1
        return True


a = Solution()
in_para1 =  [11,11,9,4,3,3,3,1,-1,-1,3,3,3,5,5,5]
in_para2 = 2
resu = a.isMonotonic(in_para1)
print(resu)
