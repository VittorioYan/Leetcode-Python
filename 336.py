from typing import List
# import sys
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_dict = {word:i for i,word in enumerate(words)}
        ans = []
        for i,word in enumerate(words):
            for j in range(len(word)+1):
                tmp1 = word[:j]
                tmp2 = word[j:]
                if tmp1[::-1] in word_dict and tmp2==tmp2[::-1]:
                    if word_dict[tmp1[::-1]]!=i:
                        ans.append([i,word_dict[tmp1[::-1]]])
                if j>0 and tmp2[::-1] in word_dict and tmp1==tmp1[::-1]:
                    if word_dict[tmp2[::-1]]!=i:
                        ans.append([word_dict[tmp2[::-1]],i])
        return ans


a = Solution()
in_para1 = ["a",""]
in_para2 = 1
resu = a.palindromePairs(in_para1)
print(resu)
