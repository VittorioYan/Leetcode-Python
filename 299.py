from typing import List


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        from collections import Counter
        c_s = Counter(secret)
        c_g = Counter(guess)
        num_a = 0
        num_b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                c_s[secret[i]] -= 1
                c_g[secret[i]] -= 1
                num_a += 1
        for key in c_s.keys():
            if key in c_g:
                num_b += min(c_g[key], c_s[key])
        return str(num_a) + 'A' + str(num_b) + 'B'


a = Solution()
in_para1 = "1123"
in_para2 = "0111"
resu = a.getHint(in_para1, in_para2)
print(resu)
