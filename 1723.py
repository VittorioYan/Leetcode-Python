from typing import List, Sequence
import collections
import bisect

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes= sorted(boxTypes,key=lambda x:x[1])
        ans = 0
        while boxTypes and truckSize:
            if boxTypes[-1][0]>=truckSize:
                ans+=boxTypes[-1][1]*truckSize
                break
            ans += boxTypes[-1][1]*boxTypes[-1][0]
            truckSize-=boxTypes[-1][0]
            boxTypes.pop()
        return ans

a = Solution()
in_para1 = [[1,3],[2,2],[3,1]]
in_para2 = 4
resu = a.maximumUnits(in_para1,in_para2)
print(resu)
