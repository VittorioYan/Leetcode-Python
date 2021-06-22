from typing import List
import heapq

class Solution:
    def permutation(self, s: str) -> List[str]:
        def add_chr_in_string(char,string):
            res = [string+char]
            for i in range(len(string)):
                res.append(string[:i]+char+string[i:])
            return res

        str_list = [s[0]]
        for ch in s[1:]:
            cur = []
            for string in str_list:
                cur+=add_chr_in_string(ch,string)
            str_list = cur
        return sorted(list(set(str_list)))


a = Solution()
in_para1 = "abc"
in_para2 =  8
resu = a.permutation(in_para1)
print(resu)
