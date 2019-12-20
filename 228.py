from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n = len(nums)
        if n == 1:
            return [str(nums[0])]
        step = max(1, n // 1000)
        result = []
        last_index = 0
        last_value = nums[0]
        nums.append(nums[0] - 1)

        def assist(cur_index, end):
            nonlocal result, last_value, last_index
            for i in range(cur_index, end):
                if nums[i] - last_value == i - last_index:
                    continue
                if i == last_index + 1:
                    result.append(str(last_value))
                    last_index = i
                    last_value = nums[i]
                    continue
                result.append(str(last_value) + '->' + str(nums[i - 1]))
                last_index = i
                last_value = nums[i]

        if step == 1:
            assist(1, n + 1)
            return result
        now_index = step
        while now_index <= n:
            if nums[now_index] - last_value != now_index - last_index:
                assist(last_index, now_index)
            now_index += step
        assist(now_index - step, n + 1)
        return result


a = Solution()
in_para1 = [0, 1, 2, 4, 5, 7]
in_para2 = 9
resu = a.summaryRanges(in_para1)
print(resu)
