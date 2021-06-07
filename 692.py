from typing import List
import collections
import bisect
import heapq
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = list(collections.Counter(words).items())
        # n = len(count)
        # heap = []
        # for i in range(n):
        #     cur = (count[i][1],count[i][0])
        #     if len(heap)<k:
        #         heapq.heappush(heap,cur)
        #     else:
        #         if heap[0][0]==cur[0]:
        #             heapq.heappush(heap,cur)
        #         elif heap[0]<cur:
        #             heapq.heapreplace(heap,cur)
        return [item[0] for item in sorted(count,key=lambda item:(-item[1],item[0]))[:k]]

a = Solution()
in_para1 = ["i", "love", "leetcode", "i", "love", "coding","leetcode"]
in_para2 = 2
resu = a.topKFrequent(in_para1,in_para2)
print(resu)
