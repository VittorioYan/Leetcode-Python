from typing import List

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort()
        if coordinates[1][0]-coordinates[0][0]==0:
            delta=-100000
        else:
            delta = (coordinates[1][1]-coordinates[0][1])/(coordinates[1][0]-coordinates[0][0])
        
        for i in range(2,len(coordinates)):
            if coordinates[i][0]-coordinates[i-1][0]==0:
                cur=-100000
            else:
                cur = (coordinates[i][1]-coordinates[i-1][1])/(coordinates[i][0]-coordinates[i-1][0])
            if cur!=delta:
                return False
        return True

a = Solution()
in_para1 =[[1,1],[2,2],[2,0]]
in_para2 = 552
resu = a.checkStraightLine(in_para1)
print(resu)
