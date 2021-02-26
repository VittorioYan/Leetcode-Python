from typing import Counter, List
import collections
import bisect
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        counter = sorted(dict(counter).items(),key=lambda a:a[1],reverse=True)
        return [a[0] for a in counter[:k]]
        
a = Solution()
in_para1 =[1,1,1,2,2,3]
in_para2 =2
resu = a.topKFrequent(in_para1,in_para2)
print(resu)
