from typing import Counter, List
import collections
import bisect
class Solution:
    def reverseVowels(self, s: str) -> str:
        # if len(s)<2:
        #     return s
        l,r = 0,len(s)-1
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        lis = list(s)
        while True:
            while l<=r and s[l] not in vowel:
                l+=1
            while l<=r and s[r] not in vowel:
                r-=1
            if l<r:
                tmp = lis[l]
                lis[l] = lis[r]
                lis[r] = tmp
                l+=1
                r-=1
            else:
                return ''.join(lis)

        
a = Solution()
in_para1 ="aA"
in_para2 = [0]
resu = a.reverseVowels(in_para1)
print(resu)
