from typing import List
# import sys


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1)==''.join(word2)


a = Solution()
in_para1 = ["abc", "d", "defg"]
in_para2 = ["abcddefg"]
resu = a.arrayStringsAreEqual(in_para1, in_para2)
print(resu)
