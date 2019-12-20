from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        len_s = len(s)
        dp = [False]*(len_s+1)
        dp[0] = True
        for i in range(len_s+1):
            for k in range(i, -1, -1):
                dp[i] = dp[i] or (dp[i-k] and s[i-k:i] in wordDict)
        print(dp)
        return dp[len_s]

a = Solution()
word_in = "catsandog"
word_dict_in = ["cats", "dog", "sand", "and", "cat"]
# cost_in = [3,4,5,1,2]
# cost_in = [4,4,1,5,1]
res = a.wordBreak(word_in, word_dict_in)
print(res)
