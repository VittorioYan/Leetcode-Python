from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        dp = {}
        tar_len = len(str(target)) + 1

        def combine(dict1: dict, dict2: dict):
            new_dic = {}
            for key1, value1 in dict1.items():
                for val1 in value1:
                    for key2, value2 in dict2.items():
                        for val2 in value2:
                            _update(new_dic, key1 + key2, val1 + '+' + val2)
                            # _update(new_dic, key1 - key2, val1 + '-' + val2)
            return new_dic

        def _update(up_dict, key, value):
            if not isinstance(value, list):
                value = [value]
            if key in up_dict:
                up_dict[key] += value
            else:
                up_dict[key] = value

        def calcu(l, r):
            cur_dic = {}
            cur_str = num[l:r]
            if cur_str in dp.keys():
                return dp[cur_str]
            if l == r:
                return {}
            if len(cur_str) == 1:
                _update(cur_dic, int(cur_str), cur_str)

            if len(cur_str) >= 2:
                a_plus = 0
                b_minus = int(cur_str[0]) * 2
                c_multi = 1
                for char in cur_str:
                    cur_int = int(char)
                    a_plus += cur_int
                    b_minus -= cur_int
                    c_multi *= cur_int
                _update(cur_dic, c_multi, '*'.join(cur_str))
                _update(cur_dic, a_plus, '+'.join(cur_str))
                _update(cur_dic, b_minus, '-'.join(cur_str))

                for i in range(l + 1, r - 1):
                    mid_dict = combine(calcu(l, i), calcu(i, r))
                    for key, value in mid_dict.items():
                        _update(cur_dic, key, value)
                    # cur_dic.update(combine(calcu(l, i), calcu(i, r), need_add))
                    # if target in cur_dic.keys():
                    #     if need_add:
                    #         res.add(cur_dic[target])
                if len(cur_str) < tar_len:
                    if cur_str[0] != '0':
                        _update(cur_dic, int(cur_str), cur_str)
            dp[cur_str] = cur_dic
            return cur_dic

        calcu(0, len(num))
        if target in dp[num].keys():
            return list(set(dp[num][target]))
        return []


a = Solution()
in_para1 = "123456"
in_para2 = 21
resu = a.addOperators(in_para1, in_para2)
print(resu)
