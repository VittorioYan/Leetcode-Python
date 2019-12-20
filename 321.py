from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_array(nums, lens):
            if not lens:
                return []
            stack, pop_num = [], len(nums) - lens
            for num in nums:
                while stack and pop_num and stack[-1] < num:
                    stack.pop()
                    pop_num -= 1
                stack.append(num)
            return stack[:lens]

        def merge(lis1, lis2):
            res = [max(lis1, lis2).pop(0) for _ in range(k)]
            return res

        ans = [0] * k
        for i in range(k + 1):
            # print(i)
            if i > len(nums1) or k - i > len(nums2):
                continue
            tmp1 = max_array(nums1, i)
            tmp2 = max_array(nums2, k - i)
            tmp = merge(tmp1, tmp2)
            if tmp > ans:
                ans = tmp

        return ans


a = Solution()
in_para1 = [3,9]
in_para2 = [8,9]
resu = a.maxNumber(in_para1, in_para2, 3)
print(resu)
