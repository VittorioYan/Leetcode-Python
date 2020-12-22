from typing import List
import collections
import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def lengthOfLIS(nums: List[List[int]]) -> int:
            tails = []
            for num in nums:
                pos = bisect.bisect_left(tails,num[1])
                if pos==len(tails):
                    tails.append(num[1])
                else:
                    tails[pos] = num[1]
            return len(tails)
            
        sort_env = sorted(envelopes,key=lambda x:[x[0],-x[1]])
        return lengthOfLIS(sort_env)
        lens = len(envelopes)
        dp = [1]*(lens)
        
        for i in range(lens):
            for j in range(i):
                if sort_env[i][1]>sort_env[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

   

        

a = Solution()
in_para1 = [[5,4],[6,4],[6,7],[2,3]]
in_para2 = "execution"
resu = a.maxEnvelopes(in_para1)
print(resu)
