from typing import List


class Solution:
    class WordDictionary:
        class Treenode:
            def __init__(self):
                self.son = {}
                self.end_flag = ""

            def change_flag(self, word):
                self.end_flag = word

        def __init__(self):
            """
            Initialize your data structure here.
            """
            self.tree = self.Treenode()

        def addWord(self, word: str) -> None:
            """
            Adds a word into the data structure.
            """
            pointer = self.tree
            for char in word:
                if char in pointer.son:
                    pointer = pointer.son[char]
                else:
                    pointer.son[char] = self.Treenode()
                    pointer = pointer.son[char]
            pointer.change_flag(word)

        def search(self, char, pointer):
            if char in pointer.son:
                return 0, pointer.son[char]
            else:
                return -1, pointer

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.WordDictionary()
        for word in words:
            trie.addWord(word)
        m, n = len(board), len(board[0])
        color = [[-1] * n for _ in range(m)]
        res = []

        def dfs(i, j, pointer):
            if color[i][j] == 0:
                return
            if board[i][j] in pointer.son:
                _next = pointer.son[board[i][j]]
                if _next.end_flag:
                    res.append(_next.end_flag)
                color[i][j] = 0
                if i - 1 >= 0:
                    dfs(i - 1, j, _next)
                if j - 1 >= 0:
                    dfs(i, j - 1, _next)
                if i + 1 < m:
                    dfs(i + 1, j, _next)
                if j + 1 < n:
                    dfs(i, j + 1, _next)
                color[i][j] = -1
            else:
                return

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.tree)
        return list(set(res))


a = Solution()
in_para1 = [
    ['o', 'a', 'a', 'p'],
    ['e', 't', 'a', 'e'],
    ['i', 'h', 'k', 'r'],
    ['i', 'f', 'l', 'v']
]
in_para2 = ["oath", "peat", "eat", "a","pea"]
resu = a.findWords(in_para1, in_para2)
print(resu)
