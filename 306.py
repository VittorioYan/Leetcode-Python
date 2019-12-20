from typing import List


class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = num1[::-1], num2[::-1]  # 将输入字符串逆序
        len1, len2 = len(num1), len(num2)  # 获得字符串长度
        res = ''  # 初始化结果变量
        carry = 0  # 初始化进位
        for i in range(max(len1, len2)):  # 开始遍历
            n1 = ord(num1[i]) - ord('0') if i < len1 else 0  # 取第一个数的当前位
            n2 = ord(num2[i]) - ord('0') if i < len2 else 0  # 取第二个数的当前位
            s = n1 + n2 + carry  # 当前位的计算结果
            carry, r = s // 10, s % 10  # 获得余数和进位
            res = str(r) + res  # 把余数加到当前结果的最高位
        if carry:  # 如果算完还有进位
            res = str(carry) + res  # 加到结果最高位
        return res

    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def recursion(last_num: str, this_num: str, point: int) -> bool:
            nonlocal n, num
            if point == n:
                return True
            if last_num[0] == '0' and len(last_num) > 1:
                return False
            if this_num[0] == '0' and len(this_num) > 1:
                return False
            next_sum = self.addStrings(last_num, this_num)
            if len(next_sum) > n - point:
                return False
            if next_sum == num[point:point + len(next_sum)]:
                if recursion(this_num, next_sum, point + len(next_sum)):
                    return True
            return False

        for i in range(1, n):
            for j in range(i + 1, n):
                if recursion(num[:i], num[i:j], j):
                    return True
        return False


a = Solution()
in_para1 = "448122032"
in_para2 = 9
resu = a.isAdditiveNumber(in_para1)
print(resu)
