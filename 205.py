from typing import List


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = {}
        for i in range(len(s)):
            if s[i] in char_dict:
                if char_dict[s[i]] != t[i]:
                    return False
            elif t[i] in char_dict.values():
                return False
            else:
                char_dict[s[i]] = t[i]
        return True


a = Solution()
in_para1 = "egg"
in_para2 = "add"
resu = a.isIsomorphic(in_para2, in_para1)
print(resu)
