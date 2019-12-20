from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        def helper(i: int, j: int):
            up = max(i - 1, 0)
            down = min(i + 1, m - 1)
            l = max(j - 1, 0)
            r = min(j + 1, n - 1)
            count = 0
            for ud in range(up, down + 1):
                for lr in range(l, r + 1):
                    if board[ud][lr] == 1:
                        if not (ud == i and lr == j):
                            count += 1
            return count

        change_pos = []

        for i in range(m):
            for j in range(n):
                cur_count = helper(i, j)
                if board[i][j] == 1:
                    if cur_count < 2:
                        change_pos.append((i, j))
                    if cur_count > 3:
                        change_pos.append((i, j))
                if board[i][j] == 0:
                    if cur_count == 3:
                        change_pos.append((i, j))
        for i, j in change_pos:
            board[i][j] = int(not board[i][j])
        print(board)


a = Solution()
in_para1 = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
in_para2 = 9
resu = a.gameOfLife(in_para1)
print(resu)
