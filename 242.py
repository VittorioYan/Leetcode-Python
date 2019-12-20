from typing import List


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        dic_s = Counter(s)
        dic_t = Counter(t)
        for key in dic_s.keys():
            if key in dic_t.keys() and dic_s[key] == dic_t[key]:
                dic_t.pop(key)
            else:
                return False
        if dic_t:
            return False
        return True


a = Solution()
in_para1 = "anagram"
in_para2 = "nagarama"
resu = a.isAnagram(in_para1, in_para2)
print(resu)
