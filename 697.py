from typing import List
import bisect
import collections
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        repeat,most_nums= 0,[]
        for key,val in count.items():
            if val>repeat:
                repeat = val
                most_nums = [key]
            elif val==repeat:
                most_nums.append(key)
        if repeat==1:
            return 1

        most_nums = set(most_nums)
        ans = len(nums)+1
        l,r = {},{}
        for index,num in enumerate(nums):
            if num in most_nums:
                if num in l:
                    r[num] = index
                else:
                    l[num] = index
        for k,v in r.items():
            ans = min(v-l[k]+1,ans)
        return ans

a = Solution()
in_para1 = [1,2,2,3,1,4,2]
in_para2 = "acde"
resu = a.findShortestSubArray(in_para1)
print(resu)
