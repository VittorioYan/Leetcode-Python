from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        res = 0
        m, n = len(grid), len(grid[0])
        def color(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if grid[i][j] == "1":
                grid[i][j] = "A"
                color(i + 1, j)
                color(i - 1, j)
                color(i, j + 1)
                color(i, j - 1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    color(i, j)
                    res += 1
        return res





a = Solution()
in_para1 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
in_para2 = 3
resu = a.numIslands(in_para1)
print(resu)