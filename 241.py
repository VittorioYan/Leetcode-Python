from typing import List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        n = len(input)
        if not input:
            return []
        symbol = [-1]
        for i in range(n):
            if input[i] == '*' or input[i] == '+' or input[i] == '-':
                symbol.append(i)
        symbol.append(n)
        sn = len(symbol)
        dp = [[[]] * (sn) for _ in range(sn)]

        def combine(lis_a, lis_b, com_symbol):
            if not lis_a or not lis_b:
                return []
            com_res = []
            for la in lis_a:
                for lb in lis_b:
                    if com_symbol == '*':
                        com_res.append(la * lb)
                    if com_symbol == '+':
                        com_res.append(la + lb)
                    if com_symbol == '-':
                        com_res.append(la - lb)
            return com_res

        def helper(l, r):
            if dp[l][r]:
                return dp[l][r]
            if r - l <= 2:
                return [eval(input[symbol[l] + 1:symbol[r]])]
            mid_res = []
            for i in range(l+1, r):
                mid_res.extend(combine(helper(l, i), helper(i, r), input[symbol[i]]))
            dp[l][r] = mid_res
            return mid_res

        return helper(0, sn-1)


a = Solution()
in_para1 = "2-1-1"
in_para2 = 9
resu = a.diffWaysToCompute(in_para1)
print(resu)
