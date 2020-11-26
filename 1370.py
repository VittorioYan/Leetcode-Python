from typing import List


class Solution:
    def sortString(self, s: str) -> str:
        s_counter = [0]*26
        for char in s:
            s_counter[ord(char)-97] += 1
        # print(s_counter)
        now_direction = True
        # now_pos = -1
        new_s = ''
        while len(new_s)<len(s):
            if now_direction:
                for i in range(26):
                    if s_counter[i]>0:
                        new_s += chr(97+i)
                        s_counter[i]-=1
                now_direction = False
            else:
                for i in range(25, -1,-1):
                    if s_counter[i] > 0:
                        new_s += chr(97+i)
                        s_counter[i] -= 1
                now_direction = True
        return new_s


a = Solution()
in_para1 = "leetcode"
in_para2 = 552
resu = a.sortString(in_para1)
print(resu)
