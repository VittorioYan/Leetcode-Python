from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        ops = set(list(['+', '-', '(', ')']))
        op_stack = []
        operand_stack = []
        last_index = 0
        s = s.strip()

        def calcu():
            nonlocal op_stack, operand_stack
            while len(op_stack) > 0 and op_stack[-1] != '(':
                a = operand_stack.pop()
                b = operand_stack.pop()
                op = op_stack.pop()
                if op == '+':
                    operand_stack.append(a + b)
                else:
                    operand_stack.append(b - a)

        for i in range(len(s)):
            if s[i] not in ops:
                continue
            if s[i] == '+' or s[i] == '-':
                if last_index < i:
                    operand_stack.append(int(s[last_index:i].replace(' ', '')))
                last_index = i + 1
                calcu()
                op_stack.append(s[i])
            if s[i] == '(':
                last_index = i + 1
                op_stack.append(s[i])
            if s[i] == ')':
                if last_index < i:
                    operand_stack.append(int(s[last_index:i].replace(' ', '')))
                last_index = i + 1
                calcu()
                op_stack.pop()

        if last_index <= len(s) - 1:
            operand_stack.append(int(s[last_index:].replace(' ', '')))
        if len(op_stack) > 0:
            calcu()
        return operand_stack[0]


a = Solution()
in_para1 = "   (  3 ) "
in_para2 = 9
resu = a.calculate(in_para1)
print(resu)
