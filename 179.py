from typing import List
import sys
import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def quiksort(arr):
            """
            实现快速排序
            :param arr:
            :return:
            """
            if len(arr) < 2:
                return arr  # 基线条件:为空或只包含一个元素的数组是“有序”的
            else:
                pivot = arr[0]  # 递归条件
                less = [x for x in arr[1:] if x+pivot <= pivot+x]  # 由所有小于基准值的元素组成的子数组

                large = [z for z in arr[1:] if z+pivot > pivot+z]  # 由所有大于基准值的元素组成的子数组

                # print('less', arr, less)
                # print('large', arr, large)
                # print('分割线'.center(30, '#'))
                return quiksort(large) + [pivot] + quiksort(less)  # 递归调用
        sort_list = []
        if not nums:
            return ''
        for num in nums:
            sort_list.append(str(num))
        sort_list = quiksort(sort_list)
        if sort_list[0] == '0':
            return "0"
        return ''.join(sort_list)



a = Solution()
in_para1 = [0,0]
in_para2 = 452137076
resu = a.largestNumber(in_para1)
print(resu)