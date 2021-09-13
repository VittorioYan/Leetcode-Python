from typing import List
import collections
import bisect
import random

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans = [0]*(n+2)
        for i,j,k in bookings:
            ans[i]+=k
            ans[j+1]-=k
        for i in range(1,n+1):
            ans[i] += ans[i-1]
        return ans[1:-1]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
            

a = Solution()
in_para1 = [[1,2,10],[2,3,20],[2,5,25]]
in_para2 = 5
resu = a.corpFlightBookings(in_para1,in_para2)
print(resu)
