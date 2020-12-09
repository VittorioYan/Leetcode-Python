from typing import List

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        _map = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                _map[i][j] = _map[i-1][j]+_map[i][j-1]
        return _map[m-1][n-1]

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         return comb(m+n-2,n-1)

a = Solution()
in_para1 = 2
in_para2 = 2
resu = a.uniquePaths(in_para1,in_para2)
print(resu)
