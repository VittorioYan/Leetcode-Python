from typing import List
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        suma,sumb = sum(A),sum(B)
        minus = (sumb-suma)//2
        setb = set(B)
        for num in A:
            if num+minus in setb:
                return [num,num+minus]



a = Solution()
in_para1 = [1,2,5]
in_para2 = [2,4]
resu = a.fairCandySwap(in_para1,in_para2)
print(resu)
