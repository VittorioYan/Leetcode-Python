from typing import List, Sequence
import collections
import bisect

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        max_len = 3
        s = s+'!'
        ans = []
        cur_index = 0
        for i in range(1,len(s)):
            if s[i] != s[cur_index]:
                if i-cur_index>=max_len:
                    ans.append([cur_index,i-1])
                cur_index = i
        return ans 

a = Solution()
in_para1 = "aaa"
in_para2 = "execution"
resu = a.largeGroupPositions(in_para1)
print(resu)
