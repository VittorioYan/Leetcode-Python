from typing import List


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        color = [[False]*n for _ in range(m)]

        def helper(x, y):
            if x >= m or y >= n:
                return False
            if color[x][y]:
                return False
            color[x][y] = True
            if matrix[x][y] == target:
                return True
            if matrix[x][y] > target:
                return False
            return helper(x + 1, y) or helper(x, y + 1)

        return helper(0, 0)


a = Solution()
in_para1 = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
in_para2 = 20
resu = a.searchMatrix(in_para1, in_para2)
print(resu)
