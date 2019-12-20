from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            result = self.binary_search_(numbers=numbers[index+1:], target=target-num, base=index+1)
            if result != -1:
                return list([index+1, result+1])

    def binary_search_(self, numbers, target, base):
        len_num = len(numbers)
        if len_num == 0:
            return -1
        mid = len_num // 2
        if target == numbers[mid]:
            return base + mid
        if len_num == 1:
            return -1
        if target > numbers[mid]:
            return self.binary_search_(numbers[mid:], target, base+mid)
        if target < numbers[mid]:
            return self.binary_search_(numbers[:mid], target, base)


a = Solution()
res = a.twoSum(numbers=[1, 2, 3, 6, 7], target=9)
# res = a.binary_search_(numbers=[1, 2, 7, 12, 15], target=3, base=0)
print(res)
