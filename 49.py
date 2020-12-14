from typing import List
import collections

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         def calcul_str2index(cur_str:str):
#             num_count_list = sorted(collections.Counter(list(cur_str)).items())
#             return str(num_count_list)
#         def dict_update(_dict:dict,k:str,v:list):
#             if k in _dict:
#                 _dict[k]+=v
#             else:
#                 _dict[k]=v
#         ans = {}
#         for cur in strs:
#             dict_update(ans,calcul_str2index(cur),[cur])
#         return list(ans.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[]]
        ans = {}
        for item in strs:
            key = tuple(sorted(item))
            ans[key] = ans.get(key,[])+[item]
        return [v for v in ans.values()]
a = Solution()
in_para1 = ["eat","tea","tan","ate","nat","bat"]
in_para2 = 9
resu = a.groupAnagrams(in_para1)
print(resu)
