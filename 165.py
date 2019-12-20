from typing import List


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        len_v1 = len(v1)
        len_v2 = len(v2)
        cur = 0
        max_size = max(len_v1, len_v2)

        def str2num(string: str):
            for i in range(len(string)):
                if string[i] != 0:
                    break
            if i == len(string):
                return 0
            return int(string[i:])

        while cur < max_size:
            if cur < len_v1:
                v1_num = str2num(v1[cur])
            else:
                v1_num = 0
            if cur < len_v2:
                v2_num = str2num(v2[cur])
            else:
                v2_num = 0
            if v1_num > v2_num:
                return 1
            if v1_num < v2_num:
                return -1
            cur += 1
        return 0


a = Solution()
in_para1 = "00120.0.1"
in_para2 = "1.10.10"
resu = a.compareVersion(in_para1, in_para2)
print(resu)