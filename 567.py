from typing import Collection, List
import bisect
import collections
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # def hash_dict(dic:dict):
        #     return str(sorted(dic.items()))

        def dec_dict(dic:dict,key:int):
            if dic[key]==1:
                dic.pop(key)
            else:
                dic[key]-=1

        def add_dict(dic:dict,key:int):
            dic[key] = dic.get(key,0)+1

        aim = dict(collections.Counter(list(s1)))
        len1,len2 = len(s1),len(s2)
        point = len1
        if len1>len2:
            return False
        cur = dict(collections.Counter(list(s2[:len1])))
        if cur == aim:
                return True
        while point<len2:
            add_dict(cur,s2[point])
            dec_dict(cur,s2[point-len1])
            if cur == aim:
                return True
            point+=1
        return False
            
            

a = Solution()
in_para1 ="ab"
in_para2 = "eidbaoook"
resu = a.checkInclusion(in_para1,in_para2)
print(resu)
