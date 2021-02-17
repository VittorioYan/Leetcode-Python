from typing import List
import bisect
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l,r ,size= 1,1,len(arr)
        trend = 1
        ans = 1
        while r<size:
            if l==r:
                if arr[r]-arr[r-1]>0:
                    trend = 1
                    r+=1
                elif arr[r]-arr[r-1]<0:
                    trend = -1
                    r+=1
                else:
                    l+=1
                    r+=1
                    continue
            else:
                if (arr[r]-arr[r-1])*trend<0:
                    r+=1
                    trend = -trend
                else:
                    ans = max(ans,r-l+1)
                    l=r
        ans = max(ans,r-l+1)
        return ans
        

a = Solution()
in_para1 = [4,8,4,16]
in_para2 = "acde"
resu = a.maxTurbulenceSize(in_para1)
print(resu)
