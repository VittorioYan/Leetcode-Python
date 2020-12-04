from typing import List
import collections

# class Solution:
#     def isPossible(self, nums: List[int]) -> bool:
#         end_dict = {}
#         need_list = []
#         def dict_minus_one(dic:dict,k:int):
#             dic[k]-=1
#             if dic[k]==0:
#                 del dic[k]

#         def isPos(nums_dict:dict):
#             for num in nums:
#                 if num+1 in nums_dict and num+2 in nums_dict:
#                     dict_minus_one(nums_dict,num)
#                     dict_minus_one(nums_dict,num+1)
#                     dict_minus_one(nums_dict,num+2)
#                     end_dict[num+2] = 1 if num+2 not in end_dict else end_dict[num+2]+1
#                 else:
#                     need_list.append(num)
#                     dict_minus_one(nums_dict,num)

#         isPos(collections.Counter(nums))
#         for n in need_list:
#             if n-1 in end_dict and end_dict[n-1]!=0:
#                 end_dict[n-1]-=1
#                 end_dict[n] = 1 if n not in end_dict else end_dict[n]+1
#             else:
#                 return False
#         return True

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        end_dict = {}
        def dict_minus_one(dic:dict,k:int):
            dic[k]-=1
            if dic[k]==0:
                del dic[k]

        def isPos(nums_dict:dict) -> bool:
            while nums_dict:
                num = min(nums_dict)
                if num-1 in end_dict:
                    end_dict[num] =1 if num not in end_dict else end_dict[num]+1
                    dict_minus_one(end_dict,num-1)
                    dict_minus_one(nums_dict,num)
                    continue
                elif num+1 in nums_dict and num+2 in nums_dict:
                    dict_minus_one(nums_dict,num)
                    dict_minus_one(nums_dict,num+1)
                    dict_minus_one(nums_dict,num+2)
                    end_dict[num+2] = 1 if num+2 not in end_dict else end_dict[num+2]+1
                else:
                    return False
            return True

        return isPos(collections.Counter(nums))
        # for n in need_list:
        #     if n-1 in end_dict and end_dict[n-1]!=0:
        #         end_dict[n-1]-=1
        #         end_dict[n] = 1 if n not in end_dict else end_dict[n]+1
        #     else:
        #         return False
        # return True

a = Solution()
in_para1 = [1,2,3,4,5]
in_para2 = 552
resu = a.isPossible(in_para1)
print(resu)
