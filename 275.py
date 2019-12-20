from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for i in range(-1, -n-1, -1):
            if citations[i] <= -i - 1:
                return -i-1
        return n


a = Solution()
in_para1 = [0]
in_para2 = 9
resu = a.hIndex(in_para1)
print(resu)
