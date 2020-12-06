from typing import List
import bisect

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        for i in range(1,numRows):
            last_row = ans[-1]
            now_row = [1]*(i+1)
            for k in range(1,i):
                now_row[k]=last_row[k]+last_row[k-1]
            ans.append(now_row)
        return ans[0:numRows]


a = Solution()
in_para1 = [2, 4, 3, 5, 1]
in_para2 = 0
resu = a.generate(in_para2)
print(resu)
