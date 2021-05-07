from typing import DefaultDict, List
import collections
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = max(weights)
        r = sum(weights)
        aim = (l+r)//2
        ans = r
        while r>l:
            cur_d = 1
            cur_sum = 0
            for weigh in weights:
                if cur_sum+weigh>aim:
                    cur_sum = 0
                    cur_d +=1
                    if cur_d>D:
                        break
                cur_sum+=weigh
            if cur_d>D:
                l = aim+1
                aim = (l+r)//2
            if cur_d<=D:
                ans = aim
                r = aim
                aim = (l+r)//2
        return ans


a = Solution()
in_para1 = [3,2,2,4,1,4]
in_para2 = 3
resu = a.shipWithinDays(in_para1,in_para2)
print(resu)
