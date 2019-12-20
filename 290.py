from typing import List


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split()
        words_dict = {}
        if len(words) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] in words_dict:
                if words[i] != words_dict[pattern[i]]:
                    return False
            else:
                if words[i] in words_dict.values():
                    return False
                words_dict[pattern[i]] = words[i]
        return True


a = Solution()
in_para1 = "abba"
in_para2 = "dog cat cat fish"
resu = a.wordPattern(in_para1, in_para2)
print(resu)
