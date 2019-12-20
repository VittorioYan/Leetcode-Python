from typing import List


class Solution:

    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        ans = []
        char_dict = Counter(s)

        for char in s:
            char_dict[char] -= 1
            if char in ans:
                continue

            i = len(ans) - 1
            remain_max = chr(ord('a')-1)
            while i >= 0:
                if ans[i] > char and char_dict[ans[i]] > 0:
                    if remain_max < ans[i]:
                        ans.pop(i)
                else:
                    remain_max = max(remain_max, ans[i])
                i -= 1
            ans += [char]

        return ''.join(ans)


a = Solution()
in_para1 = "a"
in_para2 = 9
resu = a.removeDuplicateLetters(in_para1)
print(resu)
