from typing import Counter, List, Sequence
import collections
import bisect
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        def assist(a:int):
            return abs(a-1)

        window = customers[0]*grumpy[0]
        pre = [0]*len(customers)
        max_r = X
        pre[0] = customers[0]*assist(grumpy[0])
        for i in range(1,X):
            tmp = customers[i]*assist(grumpy[i])
            pre[i] = pre[i-1]+tmp
            window+=customers[i]*grumpy[i]
        max_window = window
        for i in range(X,len(customers)):
            tmp = customers[i]*assist(grumpy[i])
            pre[i] = pre[i-1]+tmp
            window+=customers[i]*grumpy[i]
            window-=customers[i-X]*grumpy[i-X]
            if window>max_window:
                max_window = window
                max_r = i+1
        pre = [0]+pre
        return sum(customers[max_r-X:max_r])+pre[max_r-X]+(pre[-1]-pre[max_r])
                


a = Solution()
in_para1 =[1]
in_para2 = [0]
resu = a.maxSatisfied(in_para1,in_para2,1)
print(resu)
