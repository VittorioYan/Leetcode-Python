from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        len_i = len(board)
        len_j = len(board[0])
        for i in range(len_i):
            for j in range(len_j):
                if board[0][j] == 'O':
                    self.point_near(0, j, board)
                if board[i][0] == 'O':
                    self.point_near(i, 0, board)
                if board[i][len_j-1] == 'O':
                    self.point_near(i, len_j-1, board)
                if board[len_i-1][j] == 'O':
                    self.point_near(len_i-1, j, board)
        for i in range(len_i):
            for j in range(len_j):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'U':
                    board[i][j] = 'O'

    def point_near(self, x, y, board):
        board[x][y] = 'U'
        len_i = len(board)
        len_j = len(board[0])
        if x-1 > 0 and board[x-1][y] == 'O':
            self.point_near(x-1, y, board)
        if y-1 > 0 and board[x][y-1] == 'O':
            self.point_near(x, y-1, board)
        if x+1 < len_i and board[x+1][y] == 'O':
            self.point_near(x+1, y, board)
        if y+1 < len_j and board[x][y+1] == 'O':
            self.point_near(x, y+1, board)


a = Solution()
graph = [[]]
a.solve(graph)
print(graph)
