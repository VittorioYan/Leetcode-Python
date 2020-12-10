from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five,ten = 0,0
        for num in bills:
            if num==5:
                five+=1
            if num==10:
                if five<=0:
                    return False
                five-=1
                ten+=1
            if num==20:
                if ten<=0:
                    if five<=2:
                        return False
                    five-=3
                else:
                    if five<=0:
                        return False
                    five-=1
                    ten-=1
        return True


a = Solution()
in_para1 = [5,5,5,10,20]
in_para2 = 5
resu = a.lemonadeChange(in_para1)
print(resu)
