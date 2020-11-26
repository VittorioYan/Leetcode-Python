from typing import List


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        order = preorder.split(',')
        stack = []
        for point in order:
            while point == '#' and stack and stack[-1] == '#':
                stack.pop()
                if not stack:
                    return False
                stack.pop()
            stack.append(point)
        print(stack)
        return len(stack) == 1 and stack[0] == '#'


a = Solution()
in_para1 = "9,3,4,#,#,1,#,#,2,#,6,#,#"
in_para2 = 9
resu = a.isValidSerialization(in_para1)
print(resu)
