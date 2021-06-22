from typing import List, Text
import collections
import bisect

# class Solution:
#     def largestNumber(self, cost: List[int], target: int) -> str:
#         dp  = ['']*(target+1)
#         for i in range(1,10):
#             cur_cost = cost[i-1]
#             for j in range(cur_cost,target+1,cur_cost):
#                 if len(dp[j-cur_cost])+1>=len(dp[j]):
#                     dp[j] = dp[j-cur_cost]+str(i)
#         return ''.join(sorted(dp[-1],reverse=True))   

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp  = [[]]*(target+1)
        next_set = set(range(1,10))
        while next_set:
            cur_num = next_set.pop()
            cur_cost = cost[cur_num-1]
            for j in range(cur_cost,target+1):
                if len(dp[j-cur_cost])+1>=len(dp[j]):
                    if j!=cur_cost and len(dp[j-cur_cost])==0:
                        continue
                    temp = dp[j-cur_cost].copy()
                    bisect.insort(temp,-cur_num)
                    if len(temp)==len(dp[j]) and temp>=dp[j]:
                        continue
                    dp[j]=temp
                    for k in range(1,min(target-j+1,10)):
                        if k!=cur_num:
                            next_set.add(k)
        if dp[-1]:
            return ''.join([str(-item) for item in dp[-1]]) 
        return '0'



a = Solution()
in_para1 =[4,3,2,5,6,7,2,5,5]
in_para2 = 9
resu = a.largestNumber(in_para1,in_para2)
print(resu)
in_para1 =[7,6,5,5,5,6,8,7,8]
in_para2 = 12
resu = a.largestNumber(in_para1,in_para2)
print(resu)
in_para1 =[2,4,6,2,4,6,4,4,4]
in_para2 = 5
resu = a.largestNumber(in_para1,in_para2)
print(resu)
in_para1 =[6,10,15,40,40,40,40,40,40]
in_para2 = 47
resu = a.largestNumber(in_para1,in_para2)
print(resu)
