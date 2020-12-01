from typing import List
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        char_count = {}
        for s in S:
            if s in char_count:
                char_count[s][0]+=1
            else:
                char_count[s] = [1,s]
        max_s = list(char_count.values())
        heapq._heapify_max(max_s)
        max_char = heapq._heappop_max(max_s)
        ans = ""
        for _ in range(len(S)-1):
            ans += max_char[1]
            if len(max_s) ==0:
                return ""
            if max_char[0] > 1:
                mid = max_s[0]
                max_char[0]-=1
                max_s[0],max_char = max_char,mid
                heapq._siftup_max(max_s,0)
            else :
                max_char = heapq._heappop_max(max_s)

        return ans+max_char[1]


# class Solution:
#     def reorganizeString(self, S: str) -> str:
#         #思路：排序，后面的数组个数能否填满之间的空隙
#         a = list(S)
#         b = dict(collections.Counter(a))
#         c = sorted(b, key=lambda k: 0 - b[k])
#         d = []
#         for i in c:
#             d += [i] * b[i]
#         ans = [0] * len(a)

#         ans[::2] = d[:len(ans[::2])]  # 放前一半
#         ans[1::2] = d[len(ans[::2])::]  # 放后一半

#         if ans[0] == ans[1]:
#             return ""
#         else:
#             ans_str = ''
#             for i in ans:
#                 ans_str += i
#             return ans_str

a = Solution()
in_para1 = "aabb"
in_para2 = 552
resu = a.reorganizeString(in_para1)
print(resu)
