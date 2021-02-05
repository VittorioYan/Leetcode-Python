from typing import List
import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_median(a:list):
            left = (len(a)-1)//2
            right = (len(a))//2
            return (a[left]+a[right])/2

        a = sorted(nums[:k])
        ans = [get_median(a)]
        for i in range(1,len(nums)-k+1):
            a.pop(bisect.bisect_left(a,nums[i-1]))
            bisect.insort(a,nums[i+k-1])
            ans.append(get_median(a))

        return ans



a = Solution()
in_para1 = [1,3,-1,-3,5,3,6,7]
in_para2 = 3
resu = a.medianSlidingWindow(in_para1,in_para2)
print(resu)
