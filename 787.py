from typing import List
import collections
import bisect
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        route = collections.defaultdict(list)
        for edge in flights:
            start,end,val = edge
            route[start].append((end,val))
        this_q = [(src,0)]
        another_q = []
        minest = {src:0}
        for _ in range(k+1):
            for cur,price in this_q:
                for ne,p in route[cur]:
                    if ne not in minest or p+price < minest[ne]:
                        another_q.append((ne,p+price))
                        minest[ne] = p+price
            this_q = another_q
            another_q = []

        return minest[dst] if dst in minest else -1


a = Solution()
in_para1 = [[0,1,100],[1,2,100],[0,2,500]]
in_para2 = [[0, 1], [2, 3]]
resu = a.findCheapestPrice(3,in_para1,0,2,1)
print(resu)
