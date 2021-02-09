from typing import List
import bisect
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        l = r = 0
        size = len(A)
        cur_set = {}
        ans = 0

        def dec_dict(dic:dict,key:int):
            if dic[key]==1:
                dic.pop(key)
            else:
                dic[key]-=1

        def shrink_count(l,r,dic:dict):
            mid = 0
            while l<r:
                dec_dict(dic,A[l])
                if len(dic)<K:
                    return mid
                mid+=1
                l+=1
            return mid

        while r<size:
            cur_set[A[r]] = cur_set.get(A[r],0) + 1
            if len(cur_set)>K:
                while l<r:
                    dec_dict(cur_set,A[l])
                    l+=1
                    if len(cur_set)==K:
                        break
            if len(cur_set)==K:
                ans+=shrink_count(l,r,cur_set.copy())+1
            r+=1
        return ans
                    


a = Solution()
in_para1 =[1]
in_para2 = 3
resu = a.subarraysWithKDistinct(in_para1,in_para2)
print(resu)
