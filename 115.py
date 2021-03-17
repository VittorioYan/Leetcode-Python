from collections import defaultdict
from typing import DefaultDict, List
import bisect

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pos_dict = defaultdict(list)
        for index,item in enumerate(s):
            pos_dict[item].append(index)
        cur_pos = pos_dict.get(t[0],[])
        cur_count_suffix = list(range(len(cur_pos)+1))
        
        for idx,item in enumerate(t[1:]):
            if t[idx+1]==t[idx]:
                tmp_count = cur_count_suffix[:-1]
            else:
                tmp_pos = pos_dict.get(item,[])
                tmp_count = [0]*len(tmp_pos)

                for index,pos in enumerate(tmp_pos):
                    aim = bisect.bisect_left(cur_pos,pos)
                    tmp_count[index]=cur_count_suffix[aim]

                cur_pos = tmp_pos
            cur_count_suffix = [0]
            for i in tmp_count:
                cur_count_suffix.append(cur_count_suffix[-1]+i)
            if not cur_pos:
                return 0
        return cur_count_suffix[-1]
        



a = Solution()
in_para1 = "rabbbit"
in_para2 = "rabbit"
resu = a.numDistinct(in_para1,in_para2)
print(resu)
