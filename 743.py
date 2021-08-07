from typing import List, Sequence
import collections
import bisect
import itertools
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        route = collections.defaultdict(list)
        for s,e,v in times:
            route[s].append((e,v))
        sig = [float('inf')]*(n+1)
        sig[k] = 0
        queue = collections.deque([k])
        inque = set([k])
        while queue:
            cur = queue.popleft()
            inque.remove(cur)
            for e,v in route[cur]:
                if sig[e]>sig[cur]+v:
                    sig[e] = sig[cur]+v
                    if e in inque:
                        continue
                    queue.append(e)
                    inque.add(e)
                    
        ans = max(sig[1:])
        return -1 if ans==float('inf') else ans



a = Solution()
in_para1 =  [[1,2,1],[2,3,2],[1,3,4]]
in_para2 = "execution"
resu = a.networkDelayTime(in_para1,3,1)
print(resu)
