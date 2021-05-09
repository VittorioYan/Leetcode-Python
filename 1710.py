from typing import List, Sequence
import collections
import bisect
from sortedcontainers import SortedList

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # ans = SortedList([0]*k)
        # jobs.sort(reverse=True)
        # for job in jobs:
        #     cur = ans.pop(0)
        #     ans.add(cur+job)
        # return ans[-1]
        ans = [0]*k
        jobs.sort(reverse=True)
        result = sum(jobs)
        def find(jobs,i,ans):
            nonlocal result
            if i>=len(jobs):
                result = min(result,max(ans))
                return
            s = set()
            for j in range(len(ans)):
                if ans[j] in s:
                    continue
                else:
                    s.add(ans[j])
                if max(ans)>=result:
                    continue
                ans[j]+=jobs[i]
                find(jobs,i+1,ans)
                ans[j]-=jobs[i]
        find(jobs,0,ans)
        return result


a = Solution()
in_para1 = [254,256,256,254,251,256,254,253,255,251,251,255]
in_para2 = 10
resu = a.minimumTimeRequired(in_para1,in_para2)
print(resu)
