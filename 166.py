from typing import List


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        num_dict = {}
        res = ""
        if numerator == 0:
            return '0'
        if denominator == 1:
            return str(numerator)

        if numerator * denominator < 0:
            res += '-'
            numerator = abs(numerator)
            denominator = abs(denominator)

        cur_quot, cur_remain = divmod(numerator, denominator)
        res += str(cur_quot)
        if cur_remain == 0:
            return res
        res += '.'
        cur_index = len(res)
        circle = False
        while cur_remain != 0:
            if cur_remain in num_dict:
                circle = True
                break
            num_dict[cur_remain] = cur_index
            cur_remain *= 10
            cur_quot, cur_remain = divmod(cur_remain, denominator)
            res += str(cur_quot)
            cur_index += 1

        if circle:
            res = res[:num_dict[cur_remain]]+'('+res[num_dict[cur_remain]:]+')'
        return res



a = Solution()
in_para1 = -1
in_para2 = -2147483648
resu = a.fractionToDecimal(in_para1, in_para2)
print(resu)