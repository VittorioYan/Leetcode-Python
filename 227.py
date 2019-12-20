from typing import List


class Solution:
    def calculate(self, s: str) -> int:
        ops = set(list(['+', '-', '*', '/']))
        op_stack = []
        operand_stack = []
        last_index = 0
        s = s.strip()

        def calcu(priority):
            nonlocal op_stack, operand_stack
            if priority == 2:
                while len(op_stack) > 0 and (op_stack[-1] != '+' and op_stack[-1] != '-'):
                    a = operand_stack.pop()
                    b = operand_stack.pop()
                    op = op_stack.pop()
                    if op == '*':
                        operand_stack.append(b * a)
                    elif op == '/':
                        operand_stack.append(b // a)
                return
            while len(op_stack) > 0:
                a = operand_stack.pop()
                b = operand_stack.pop()
                op = op_stack.pop()
                if op == '+':
                    operand_stack.append(b + a)
                elif op == '-':
                    operand_stack.append(b - a)
                elif op == '*':
                    operand_stack.append(b * a)
                elif op == '/':
                    operand_stack.append(b // a)

        for i in range(len(s)):
            if s[i] not in ops:
                continue
            if s[i] == '+' or s[i] == '-':
                if last_index < i:
                    operand_stack.append(int(s[last_index:i].replace(' ', '')))
                last_index = i + 1
                calcu(0)
                op_stack.append(s[i])
            if s[i] == '*' or s[i] == '/':
                if last_index < i:
                    operand_stack.append(int(s[last_index:i].replace(' ', '')))
                last_index = i + 1
                calcu(2)
                op_stack.append(s[i])

        if last_index <= len(s) - 1:
            operand_stack.append(int(s[last_index:].replace(' ', '')))
        calcu(0)
        return operand_stack[0]


a = Solution()
in_para1 = " 3+5 / 2 "
in_para2 = 9
resu = a.calculate(in_para1)
print(resu)
