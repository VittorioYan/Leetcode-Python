from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        visited = set()
        res = set()
        for i in range(0, len(s) - 9):
            tmp = s[i:i+10]
            if tmp in visited:
                res.add(tmp)
            visited.add(tmp)
        return list(res)

a = Solution()
in_para1 = "AAAAACCCCCAAAAACCCCCAAAAAGGGTTT"
in_para2 = 452137076
resu = a.findRepeatedDnaSequences(in_para1)
print(resu)