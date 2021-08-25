from typing import List
import collections
import bisect
class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('')
        ans = 0
        cur_pos = 0
        cur_char = chars[0]
        n = len(chars)
        for i in range(1,n):
            if chars[i]!=cur_char:
                if i-cur_pos==1:
                    chars[ans] = cur_char
                    ans+=1
                else:
                    tmp = list(str(i-cur_pos))
                    chars[ans:ans+1+len(tmp)] = [cur_char]+tmp
                    ans+=1+len(tmp)
                cur_pos = i
                cur_char = chars[i]
                
        return ans


a = Solution()
in_para1 = ["a","b","c"]
in_para2 = [[0, 1], [2, 3]]
resu = a.compress(in_para1)
print(resu)
