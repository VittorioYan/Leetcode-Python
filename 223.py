from typing import List


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        a_area = (C - A) * (D - B)
        b_area = (G - E) * (H - F)
        if C <= E or H <= B or G <= A or D <= F:
            return a_area + b_area
        else:
            minus_area = (min(D, H) - max(F, B)) * (min(C, G) - max(A, E))
            return a_area + b_area - minus_area


a = Solution()
in_para1 = [1, 2, 3, 1]
in_para2 = 9
resu = a.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)
print(resu)
