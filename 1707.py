import re
from typing import List
# import sys
import heapq
import collections
import math
# 暴力方法超时
# class Solution:
#     def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
#         nums.sort()
#         index = sorted(range(len(queries)),key=lambda i:queries[i][1]) 
#         ans = [-1]*len(queries)
#         idx = 0
#         for num in nums:
#             for i in range(idx,len(index)):
#                 if queries[index[i]][1]<num:
#                     idx = i
#                 else:
#                     ans[index[i]] = max(ans[index[i]],num^queries[index[i]][0])
#         # print(index)
#         return ans

# 前缀树也有一个点过不去，我怀疑是在为难我-0-，python效率是低啊
class TrieNode:
    def __init__(self):
        self.s = ''
        self.next = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def get_root(self)->TrieNode:
        return self.root
    
    def add_str(self,new_str:str):
        cur = self.root
        for index,item in enumerate(new_str):
            if item not in cur.next:
                new_node = TrieNode()
                new_node.s = new_str[:index+1]
                cur.next[item] = new_node
            cur = cur.next[item]
        cur.is_end = True


def num_to_bin(num:int,depth:int)->str:
    b = bin(num)[2:]
    return '0'*(depth-len(b))+b

def bin32_to_num(s:str)->int:
    ans = 0
    nums = [4294967296, 2147483648, 1073741824, 536870912, 268435456, 134217728, 67108864, 33554432, 16777216, 8388608, 4194304, 2097152, 1048576, 524288, 262144, 131072, 65536, 32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    for i in range(1,len(s)+1):
        ans+=int(s[-i])*nums[-i]
    return ans
  
def find_max(tree:Trie,num:int,depth:int):
    s = num_to_bin(num,depth)
    s = s[len(s)-depth:]
    cur = tree.get_root()
    for item in s:
        if item =='1':
            if '0' in cur.next:
                cur = cur.next['0']
            else:
                cur = cur.next['1']
        else:
            if '1' in cur.next:
                cur = cur.next['1']
            else:
                cur = cur.next['0']
    return bin32_to_num(cur.s)^num

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        index = sorted(range(len(queries)),key=lambda i:queries[i][1])
        depth = len(bin(nums[-1]))-2

        i = 0
        flag = True
        ans = [0]*len(queries)
        tree = Trie()
        for num in nums:
            while i<len(queries) and queries[index[i]][1]<num:
                if flag:
                    ans[index[i]] = -1
                else:
                    ans[index[i]] = find_max(tree,queries[index[i]][0],depth)
                i+=1
            flag = False
            tree.add_str(num_to_bin(num,depth))
        while i<len(queries):
            ans[index[i]] = find_max(tree,queries[index[i]][0],depth)
            i+=1
        return ans

        

a = Solution()
in_para1 = [0,1,2,3,4]

in_para2 =  [[3,1],[1,3],[5,6]]
resu = a.maximizeXor(in_para1,in_para2)
print(resu)
