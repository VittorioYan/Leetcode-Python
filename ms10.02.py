from collections import defaultdict
from typing import Counter, List
import heapq
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def which_key(inp:str)->str:
            return ''.join(sorted(inp))
        ans = defaultdict(list)
        for s in strs:
            ans[which_key(s)].append(s)
        return list(ans.values())
            

a = Solution()
in_para1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
in_para2 = 9
resu = a.groupAnagrams(in_para1)
print(resu)
