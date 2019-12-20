from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        color = [[0] * n for _ in range(m)]
        max_length = 0

        def dfs(i, j, length):
            nonlocal color, m, n, max_length
            if color[i][j] > 0:
                return length + color[i][j]
            length += 1
            up = down = left = right = 0
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                up = length + dfs(i - 1, j, 0)
            if i + 1 < m and matrix[i + 1][j] > matrix[i][j]:
                down = length + dfs(i + 1, j, 0)
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                left = length + dfs(i, j - 1, 0)
            if j + 1 < n and matrix[i][j + 1] > matrix[i][j]:
                right = length + dfs(i, j + 1, 0)
            color[i][j] = max(up, down, left, right, 1)
            max_length = max(max_length, color[i][j])
            return color[i][j]

        for i in range(m):
            for j in range(n):
                dfs(i, j, 0)
        return max_length


a = Solution()
in_para1 = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
in_para2 = 9
resu = a.longestIncreasingPath(in_para1)
print(resu)
