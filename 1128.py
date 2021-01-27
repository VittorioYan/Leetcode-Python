from typing import List
import heapq

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def list_to_key(li:list):
            return (min(li),max(li))
        dic = {}
        ans = 0
        for domino in dominoes:
            k = list_to_key(domino)
            dic[k] = dic.get(k,0)+1
        for val in dic.values():
            if val==1:
                continue
            ans+=(val)*(val-1)//2
        return ans

a = Solution()
in_para1 = [[1,2],[2,1],[2,1],[3,4],[5,6]]
in_para2 = 806
resu = a.numEquivDominoPairs(in_para1)
print(resu)
