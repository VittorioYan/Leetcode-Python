from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        s_len = len(s)
        max_len = 0
        for word in wordDict:
            max_len = max(max_len, len(word))
        # dp = ['']*(s_len+1)
        len_s = len(s)
        dp = [False]*(len_s+1)
        dp[0] = True
        for i in range(len_s+1):
            for k in range(i, -1, -1):
                dp[i] = dp[i] or (dp[i-k] and s[i-k:i] in wordDict)
        if not dp[len_s]:
            return res

        def dfs(route, strs):
            if not strs:
                res.append(route[:-1])
            for i in range(1, len(strs)+1):
                if i > max_len:
                    break
                if strs[:i] in wordDict:
                    dfs(route+strs[:i]+' ', strs[i:])
        dfs('', s)
        return res


a = Solution()
word_in = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
word_dict_in = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
# cost_in = [3,4,5,1,2]
# cost_in = [4,4,1,5,1]
res = a.wordBreak(word_in, word_dict_in)
print(res)
