from typing import DefaultDict, List, Sequence
import collections
import bisect

# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         word_dict = DefaultDict(int)
#         def hash_word(word:str):
#             tmp = 0
#             for c in word:
#                 tmp |= 1 << (ord(c) - ord('a'))
#             return tmp

#         for word in words:
#             word_dict[hash_word(word)]+=1
        
#         def subset(word:str):
#             tmp = [""]
#             for i in word:
#                 tmp+=[i+k for k in tmp]
#             return tmp

#         ans = [0]*len(puzzles)
#         for i,p in enumerate(puzzles):
#             tmp = 0
#             subs = subset(p[1:])
#             for s in subs:
#                 tmp+= word_dict[hash_word(p[0]+s)]
#             ans[i] = tmp
#         return ans
# 100%做法，通过位运算求子集
class Solution:
    # [1] 开始
    def getMask(self, word):
        mask = 0
        for c in word:
            mask |= 1 << (ord(c) - ord('a'))
        return mask
    # [1] 结束

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        # [2] 开始
        words = [self.getMask(w) for w in words]
        d = {}
        for w in words:
            d[w] = d.get(w, 0) + 1
        # [2] 结束

        ans = []
        for p in puzzles:
            mask = self.getMask(p)
            sub_mask = mask
            head_mask = 1 << (ord(p[0]) - ord('a'))
            cnt = 0
            # [3] 开始
            while sub_mask:
                # [4] 开始
                if sub_mask & head_mask:
                    cnt += d.get(sub_mask, 0)
                # [4] 结束
                sub_mask = (sub_mask-1)&mask
            # [3] 结束
            ans.append(cnt)
        return ans

a = Solution()
in_para1 = ["aaaa","asas","able","ability","actt","actor","access"]
in_para2 = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
resu = a.findNumOfValidWords(in_para1,in_para2)
print(resu)
