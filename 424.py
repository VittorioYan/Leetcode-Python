from typing import List
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = [0]*26
        left,right,ans = 0,0,0
        while True:
            if right-left-max(char_count)>k:
                char_count[ord(s[left])-65]-=1
                left+=1
                continue
            ans = max(ans,right-left)
            if right==len(s):
                break
            char_count[ord(s[right])-65]+=1
            right+=1
        return ans

a = Solution()
in_para1 = "ABAB"
in_para2 = 2
resu = a.characterReplacement(in_para1,in_para2)
print(resu)
