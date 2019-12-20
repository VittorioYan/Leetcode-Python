from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)

        def has_common(str1: str, str2: str):
            for char in str1:
                if char in str2:
                    return True
            return False

        ans = 0
        sqrt_ans = 0
        words.sort(key=lambda x: -len(x))
        bit_cal = []
        for word in words:
            cur_res = 0
            for char in word:
                cur_res |= 1 << (ord(char) - 97)
            bit_cal.append(cur_res)

        for i in range(n):
            if len(words[i]) <= sqrt_ans:
                break
            for j in range(i + 1, n):
                if len(words[i]) * len(words[j]) <= ans:
                    break
                # if not has_common(words[i], words[j]):
                if not bit_cal[i]&bit_cal[j]:
                    ans = len(words[i]) * len(words[j])
                    sqrt_ans = int(ans ** 0.5)
        # print(words)
        return ans


a = Solution()
in_para1 = ["abcw","baz","foo","bar","xtfn","abcdef"]
in_para2 = 9
resu = a.maxProduct(in_para1)
print(resu)
