from typing import DefaultDict, List, Sequence
import collections
import bisect
import itertools

class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        n = len(target)
        tar2idx = {}
        for idx,tar in enumerate(target):
            tar2idx[tar] = idx
        new_arr = []
        tails = []
        for i in range(len(arr)):
            if arr[i] in tar2idx:
                new_arr.append(tar2idx[arr[i]])
        
        for num in new_arr:
            pos = bisect.bisect_left(tails,num)
            if pos==len(tails):
                tails.append(num)
            else:
                tails[pos] = num
            

        return n-len(tails)
        


a = Solution()
in_para1 =  [16,7,20,11,15,13,10,14,6,8]
in_para2 = [11,14,15,7,5,5,6,10,11,6]
resu = a.minOperations(in_para1,in_para2)
print(resu)
