from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i] <= i:
                return i
        return len(citations)


a = Solution()
in_para1 = [0]
in_para2 = 9
resu = a.hIndex(in_para1)
print(resu)
