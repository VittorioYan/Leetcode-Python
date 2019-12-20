from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if not tokens:
            return 0
        def calcu(operator):
            num2 = stack.pop()
            num1 = stack.pop()
            if operator == '+':
                res = num1+num2
            if operator == '-':
                res = num1-num2
            if operator == '*':
                res = num1*num2
            if operator == '/':
                res = int(num1/num2)
            stack.append(res)

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                calcu(token)
            else:
                stack.append(int(token))
        return stack[0]


a = Solution()
in_para1 =[]
resu = a.evalRPN(in_para1)
print(resu)