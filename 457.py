from typing import List
from collections import deque,defaultdict

class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        begin = 0
        begin_str = '0'
        n = len(nums)
        for i in range(n):
            if type(nums[i])==int:
                nex = i
                begin = nums[i]
                begin_str = str(i)
                nx_count = 0
                while type(nums[nex])==int and begin*nums[nex]>0:
                    if nums[nex]==n:
                        nums[nex] = begin_str
                        nx_count = 1
                        break
                    new = (nex+nums[nex])%n
                    nums[nex] = begin_str
                    nex = new
                if nums[nex]==begin_str and nx_count!=1:
                    return True
        return False

a = Solution()
in_para1 = [-1,-1,-1]

in_para2 = [2,4]
resu = a.circularArrayLoop(in_para1)
print(resu)
