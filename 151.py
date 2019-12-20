class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.strip().split()
        word_list.reverse()
        res = ""
        for word in word_list:
            res += word + ' '
        return res[:-1]

a = Solution()
in_para1 ="the sky is blue"
resu = a.reverseWords(in_para1)
print(resu)
