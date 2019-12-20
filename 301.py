from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        res = []
        min_reduce_num = len(s)

        def dfs(string: str, number: int, left_right_num: int, reduce_num: int):
            nonlocal res
            nonlocal min_reduce_num
            n = len(string)
            if reduce_num > min_reduce_num:
                return
            if left_right_num < 0:
                return
            if number == len(string):
                if left_right_num == 0:
                    res.append(string)
                    min_reduce_num = min(min_reduce_num,reduce_num)
                return

            if string[number] == '(':
                dfs(string, number + 1, left_right_num + 1, reduce_num)
                if number + 1 < n:
                    dfs(string[0:number] + string[number + 1:], number, left_right_num, reduce_num + 1)
                else:
                    dfs(string[0:number], number, left_right_num, reduce_num + 1)

            elif string[number] == ')':
                dfs(string, number + 1, left_right_num - 1, reduce_num)
                if number + 1 < n:
                    dfs(string[0:number] + string[number + 1:], number, left_right_num, reduce_num + 1)
                else:
                    dfs(string[0:number], number, left_right_num, reduce_num + 1)

            else:
                dfs(string, number + 1, left_right_num, reduce_num)

        dfs(s, 0, 0, 0)
        return list(set(res))


a = Solution()
in_para1 = ")("
in_para2 = 9
resu = a.removeInvalidParentheses(in_para1)
print(resu)
